import functools
import typing

import boto3
import hyperlink

from botocore import UNSIGNED
from botocore.config import Config

from botocore.handlers import disable_signing

ACCOUNT_NAMES = {
    "760097843905": "platform",
    "299497370133": "workflow",
    "975596993436": "storage",
}


@functools.cache
def get_aws_session(*, role_arn):
    # sts_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))
    sts_client = boto3.client("sts")
    assumed_role_object = sts_client.assume_role(
        RoleArn=role_arn, RoleSessionName="AssumeRoleSession1"
    )
    credentials = assumed_role_object["Credentials"]

    return boto3.Session(
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )


def guess_account(s3_identifier, role_name):
    resource = boto3.resource("s3")
    resource.meta.client.meta.events.register("choose-signer.s3.*", disable_signing)

    """
    Given the name of an S3 bucket, guess the account it belongs to.

    You can pass the name of the bucket, or the S3 URI.

    Examples:

        > guess_account('s3://example-bucket/cat.jpg')
        {'account_id': '1234567890', 'name': 'example'}

        > guess_account('example-bucket')
        {'account_id': '1234567890', 'name': 'example'}

    """
    if "wellcomedigitalworkflow" in s3_identifier:
        account_id = "299497370133"
    elif "wellcomecollection-storage" in s3_identifier:
        account_id = "975596993436"
    elif (
        "wellcomecollection-assets-workingstorage" in s3_identifier
        or "wellcomecollection-platform" in s3_identifier
        or "wellcomecollection-editorial-photography" in s3_identifier
    ):
        account_id = "760097843905"
    else:
        return None

    account_name = ACCOUNT_NAMES[account_id]

    return {
        "account_id": account_id,
        "name": account_name,
        "role_arn": f"arn:aws:iam::{account_id}:role/{account_name}-{role_name}",
    }


def create_s3_session(s3_identifier, *, role_name="read_only"):
    account = guess_account(s3_identifier, role_name)
    if account:
        return get_aws_session(role_arn=account["role_arn"])
    else:
        return boto3.Session()


class S3Uri(typing.TypedDict):
    Bucket: str
    Path: str


def parse_s3_uri(s3_uri: str) -> S3Uri:
    uri = hyperlink.parse(s3_uri)

    if uri.scheme != "s3":
        raise ValueError(f"Unrecognised scheme in {s3_uri!r}, expected s3://")

    bucket = uri.host
    path = "/".join(uri.path)

    return {"Bucket": bucket, "Path": path}


def create_link_text(*, url, label):
    # Based on https://stackoverflow.com/a/71309268/1558022

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
    return f"\033]8;;{url}\033\\{label}\033]8;;\033\\"

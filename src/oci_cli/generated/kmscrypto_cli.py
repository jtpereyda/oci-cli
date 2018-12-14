# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from .. import cli_util
from .. import json_skeleton_utils
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias
from . import kms_service_cli


@click.command(cli_util.override('kms_crypto_root_group.command_name', 'kms-crypto'), cls=CommandGroupWithAlias, help=cli_util.override('kms_crypto_root_group.help', """API for managing and performing operations with keys and vaults."""), short_help=cli_util.override('kms_crypto_root_group.short_help', """Key Management Service API"""))
@cli_util.help_option_group
def kms_crypto_root_group():
    pass


@click.command(cli_util.override('decrypted_data_group.command_name', 'decrypted-data'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def decrypted_data_group():
    pass


@click.command(cli_util.override('generated_key_group.command_name', 'generated-key'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def generated_key_group():
    pass


@click.command(cli_util.override('encrypted_data_group.command_name', 'encrypted-data'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def encrypted_data_group():
    pass


kms_service_cli.kms_service_group.add_command(kms_crypto_root_group)
kms_crypto_root_group.add_command(decrypted_data_group)
kms_crypto_root_group.add_command(generated_key_group)
kms_crypto_root_group.add_command(encrypted_data_group)


@decrypted_data_group.command(name=cli_util.override('decrypt.command_name', 'decrypt'), help="""Decrypts data using the given DecryptDataDetails resource.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--ciphertext', required=True, help="""The encrypted data to decrypt.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key used to encrypt the ciphertext.""")
@cli_util.option('--associated-data', type=custom_types.CLI_COMPLEX_TYPE, help="""Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associatedData must be fewer than 4096 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'associated-data': {'module': 'key_management', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'associated-data': {'module': 'key_management', 'class': 'dict(str, string)'}}, output_type={'module': 'key_management', 'class': 'DecryptedData'})
@cli_util.wrap_exceptions
def decrypt(ctx, from_json, ciphertext, key_id, associated_data):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['ciphertext'] = ciphertext
    details['keyId'] = key_id

    if associated_data is not None:
        details['associatedData'] = cli_util.parse_json_parameter("associated_data", associated_data)

    client = cli_util.build_client('kms_crypto', ctx)
    result = client.decrypt(
        decrypt_data_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@encrypted_data_group.command(name=cli_util.override('encrypt.command_name', 'encrypt'), help="""Encrypts data using the given EncryptDataDetails resource. Plaintext included in the example request is a base64-encoded value of a UTF-8 string.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the key to encrypt with.""")
@cli_util.option('--plaintext', required=True, help="""The plaintext data to encrypt.""")
@cli_util.option('--associated-data', type=custom_types.CLI_COMPLEX_TYPE, help="""Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associatedData must be fewer than 4096 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'associated-data': {'module': 'key_management', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'associated-data': {'module': 'key_management', 'class': 'dict(str, string)'}}, output_type={'module': 'key_management', 'class': 'EncryptedData'})
@cli_util.wrap_exceptions
def encrypt(ctx, from_json, key_id, plaintext, associated_data):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['keyId'] = key_id
    details['plaintext'] = plaintext

    if associated_data is not None:
        details['associatedData'] = cli_util.parse_json_parameter("associated_data", associated_data)

    client = cli_util.build_client('kms_crypto', ctx)
    result = client.encrypt(
        encrypt_data_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@generated_key_group.command(name=cli_util.override('generate_data_encryption_key.command_name', 'generate-data-encryption-key'), help="""Generates a key that you can use to encrypt or decrypt data.

The top level --endpoint parameter must be supplied for this operation.""")
@cli_util.option('--include-plaintext-key', required=True, type=click.BOOL, help="""If true, the generated key is also returned unencrypted.""")
@cli_util.option('--key-id', required=True, help="""The OCID of the master encryption key to encrypt the generated data encryption key with.""")
@cli_util.option('--key-shape', required=True, type=custom_types.CLI_COMPLEX_TYPE, help="""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--associated-data', type=custom_types.CLI_COMPLEX_TYPE, help="""Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associatedData must be fewer than 4096 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'associated-data': {'module': 'key_management', 'class': 'dict(str, string)'}, 'key-shape': {'module': 'key_management', 'class': 'KeyShape'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'associated-data': {'module': 'key_management', 'class': 'dict(str, string)'}, 'key-shape': {'module': 'key_management', 'class': 'KeyShape'}}, output_type={'module': 'key_management', 'class': 'GeneratedKey'})
@cli_util.wrap_exceptions
def generate_data_encryption_key(ctx, from_json, include_plaintext_key, key_id, key_shape, associated_data):
    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['includePlaintextKey'] = include_plaintext_key
    details['keyId'] = key_id
    details['keyShape'] = cli_util.parse_json_parameter("key_shape", key_shape)

    if associated_data is not None:
        details['associatedData'] = cli_util.parse_json_parameter("associated_data", associated_data)

    client = cli_util.build_client('kms_crypto', ctx)
    result = client.generate_data_encryption_key(
        generate_key_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)

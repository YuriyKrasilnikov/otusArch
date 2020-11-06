# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/command/web_client/command_webclient.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/command/web_client/command_webclient.proto',
  package='api.command.webclient.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0proto/command/web_client/command_webclient.proto\x12\x18\x61pi.command.webclient.v1\x1a google/protobuf/field_mask.proto\"!\n\x0eStatusResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"q\n\x0bProfileData\x12,\n\x08modified\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"\x19\n\x08PaidData\x12\r\n\x05value\x18\x01 \x01(\t2\xa0\x02\n\x07Profile\x12[\n\x06Insert\x12%.api.command.webclient.v1.ProfileData\x1a(.api.command.webclient.v1.StatusResponse0\x01\x12[\n\x06Update\x12%.api.command.webclient.v1.ProfileData\x1a(.api.command.webclient.v1.StatusResponse0\x01\x12[\n\x06Remove\x12%.api.command.webclient.v1.ProfileData\x1a(.api.command.webclient.v1.StatusResponse0\x01\x32\x63\n\x07\x42illing\x12X\n\x06Insert\x12\".api.command.webclient.v1.PaidData\x1a(.api.command.webclient.v1.StatusResponse0\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='api.command.webclient.v1.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='api.command.webclient.v1.StatusResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=145,
)


_PROFILEDATA = _descriptor.Descriptor(
  name='ProfileData',
  full_name='api.command.webclient.v1.ProfileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='modified', full_name='api.command.webclient.v1.ProfileData.modified', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='api.command.webclient.v1.ProfileData.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='api.command.webclient.v1.ProfileData.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='api.command.webclient.v1.ProfileData.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=260,
)


_PAIDDATA = _descriptor.Descriptor(
  name='PaidData',
  full_name='api.command.webclient.v1.PaidData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='api.command.webclient.v1.PaidData.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=287,
)

_PROFILEDATA.fields_by_name['modified'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['ProfileData'] = _PROFILEDATA
DESCRIPTOR.message_types_by_name['PaidData'] = _PAIDDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'proto.command.web_client.command_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.command.webclient.v1.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

ProfileData = _reflection.GeneratedProtocolMessageType('ProfileData', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEDATA,
  '__module__' : 'proto.command.web_client.command_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.command.webclient.v1.ProfileData)
  })
_sym_db.RegisterMessage(ProfileData)

PaidData = _reflection.GeneratedProtocolMessageType('PaidData', (_message.Message,), {
  'DESCRIPTOR' : _PAIDDATA,
  '__module__' : 'proto.command.web_client.command_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.command.webclient.v1.PaidData)
  })
_sym_db.RegisterMessage(PaidData)



_PROFILE = _descriptor.ServiceDescriptor(
  name='Profile',
  full_name='api.command.webclient.v1.Profile',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=290,
  serialized_end=578,
  methods=[
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='api.command.webclient.v1.Profile.Insert',
    index=0,
    containing_service=None,
    input_type=_PROFILEDATA,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='api.command.webclient.v1.Profile.Update',
    index=1,
    containing_service=None,
    input_type=_PROFILEDATA,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='api.command.webclient.v1.Profile.Remove',
    index=2,
    containing_service=None,
    input_type=_PROFILEDATA,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROFILE)

DESCRIPTOR.services_by_name['Profile'] = _PROFILE


_BILLING = _descriptor.ServiceDescriptor(
  name='Billing',
  full_name='api.command.webclient.v1.Billing',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=580,
  serialized_end=679,
  methods=[
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='api.command.webclient.v1.Billing.Insert',
    index=0,
    containing_service=None,
    input_type=_PAIDDATA,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLING)

DESCRIPTOR.services_by_name['Billing'] = _BILLING

# @@protoc_insertion_point(module_scope)
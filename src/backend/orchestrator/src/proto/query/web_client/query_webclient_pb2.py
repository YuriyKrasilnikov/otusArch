# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/query/web_client/query_webclient.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/query/web_client/query_webclient.proto',
  package='api.query.webclient.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,proto/query/web_client/query_webclient.proto\x12\x16\x61pi.query.webclient.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"V\n\x0bProfileData\x12\x11\n\tcreatedAt\x18\x01 \x01(\t\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"H\n\x0fProfileDataList\x12\x35\n\x08profiles\x18\x01 \x03(\x0b\x32#.api.query.webclient.v1.ProfileData\"|\n\x0fProfilesRequest\x12=\n\x0cprofilesData\x18\x01 \x01(\x0b\x32\'.api.query.webclient.v1.ProfileDataList\x12*\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"P\n\x0b\x42illingData\x12\x10\n\x08updateAt\x18\x01 \x01(\t\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"H\n\x0f\x42illingDataList\x12\x35\n\x08\x62illings\x18\x01 \x03(\x0b\x32#.api.query.webclient.v1.BillingData\"|\n\x0f\x42illingsRequest\x12=\n\x0c\x62illingsData\x18\x01 \x01(\x0b\x32\'.api.query.webclient.v1.BillingDataList\x12*\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"g\n\x16\x42illingsCursorResponse\x12=\n\x0c\x62illingsData\x18\x01 \x01(\x0b\x32\'.api.query.webclient.v1.BillingDataList\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\t\"{\n\x06\x46ilter\x12/\n\x03key\x18\x01 \x01(\x0e\x32\".api.query.webclient.v1.BillingKey\x12\x30\n\x07operand\x18\x02 \x01(\x0e\x32\x1f.api.query.webclient.v1.Operand\x12\x0e\n\x06values\x18\x03 \x03(\t\"q\n\x08Ordering\x12/\n\x03key\x18\x01 \x01(\x0e\x32\".api.query.webclient.v1.BillingKey\x12\x34\n\tdirection\x18\x02 \x01(\x0e\x32!.api.query.webclient.v1.Direction\"\x9d\x01\n\x19\x42illingsPaginationRequest\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\x12/\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x1e.api.query.webclient.v1.Filter\x12\x30\n\x06orders\x18\x03 \x03(\x0b\x32 .api.query.webclient.v1.Ordering\x12\r\n\x05limit\x18\x04 \x01(\x05*M\n\nBillingKey\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tCREATEDAT\x10\x01\x12\x0c\n\x08NICKNAME\x10\x02\x12\t\n\x05VALUE\x10\x03\x12\n\n\x06STATUS\x10\x04*V\n\x07Operand\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02IN\x10\x01\x12\x07\n\x03OUT\x10\x02\x12\x08\n\x04LESS\x10\x03\x12\x0b\n\x07GREATER\x10\x04\x12\n\n\x06\x45QLESS\x10\x05\x12\r\n\tEQGREATER\x10\x06*&\n\tDirection\x12\x07\n\x03NOT\x10\x00\x12\x07\n\x03MIN\x10\x01\x12\x07\n\x03MAX\x10\x02\x32\xb1\x01\n\x07Profile\x12W\n\x03Get\x12\'.api.query.webclient.v1.ProfilesRequest\x1a\'.api.query.webclient.v1.ProfileDataList\x12M\n\x0eIdentification\x12\x16.google.protobuf.Empty\x1a#.api.query.webclient.v1.ProfileData2b\n\x07\x42illing\x12W\n\x03Get\x12\'.api.query.webclient.v1.BillingsRequest\x1a\'.api.query.webclient.v1.BillingDataList2z\n\x0e\x42illingHistory\x12h\n\x03Get\x12\x31.api.query.webclient.v1.BillingsPaginationRequest\x1a..api.query.webclient.v1.BillingsCursorResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])

_BILLINGKEY = _descriptor.EnumDescriptor(
  name='BillingKey',
  full_name='api.query.webclient.v1.BillingKey',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATEDAT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NICKNAME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1210,
  serialized_end=1287,
)
_sym_db.RegisterEnumDescriptor(_BILLINGKEY)

BillingKey = enum_type_wrapper.EnumTypeWrapper(_BILLINGKEY)
_OPERAND = _descriptor.EnumDescriptor(
  name='Operand',
  full_name='api.query.webclient.v1.Operand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GREATER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EQLESS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EQGREATER', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1289,
  serialized_end=1375,
)
_sym_db.RegisterEnumDescriptor(_OPERAND)

Operand = enum_type_wrapper.EnumTypeWrapper(_OPERAND)
_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='api.query.webclient.v1.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAX', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1377,
  serialized_end=1415,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
UNKNOWN = 0
CREATEDAT = 1
NICKNAME = 2
VALUE = 3
STATUS = 4
NONE = 0
IN = 1
OUT = 2
LESS = 3
GREATER = 4
EQLESS = 5
EQGREATER = 6
NOT = 0
MIN = 1
MAX = 2



_PROFILEDATA = _descriptor.Descriptor(
  name='ProfileData',
  full_name='api.query.webclient.v1.ProfileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='createdAt', full_name='api.query.webclient.v1.ProfileData.createdAt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='api.query.webclient.v1.ProfileData.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='api.query.webclient.v1.ProfileData.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='api.query.webclient.v1.ProfileData.description', index=3,
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
  serialized_start=135,
  serialized_end=221,
)


_PROFILEDATALIST = _descriptor.Descriptor(
  name='ProfileDataList',
  full_name='api.query.webclient.v1.ProfileDataList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='profiles', full_name='api.query.webclient.v1.ProfileDataList.profiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=223,
  serialized_end=295,
)


_PROFILESREQUEST = _descriptor.Descriptor(
  name='ProfilesRequest',
  full_name='api.query.webclient.v1.ProfilesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='profilesData', full_name='api.query.webclient.v1.ProfilesRequest.profilesData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='api.query.webclient.v1.ProfilesRequest.fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=297,
  serialized_end=421,
)


_BILLINGDATA = _descriptor.Descriptor(
  name='BillingData',
  full_name='api.query.webclient.v1.BillingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='updateAt', full_name='api.query.webclient.v1.BillingData.updateAt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='api.query.webclient.v1.BillingData.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.query.webclient.v1.BillingData.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.query.webclient.v1.BillingData.status', index=3,
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
  serialized_start=423,
  serialized_end=503,
)


_BILLINGDATALIST = _descriptor.Descriptor(
  name='BillingDataList',
  full_name='api.query.webclient.v1.BillingDataList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billings', full_name='api.query.webclient.v1.BillingDataList.billings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=505,
  serialized_end=577,
)


_BILLINGSREQUEST = _descriptor.Descriptor(
  name='BillingsRequest',
  full_name='api.query.webclient.v1.BillingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billingsData', full_name='api.query.webclient.v1.BillingsRequest.billingsData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='api.query.webclient.v1.BillingsRequest.fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=579,
  serialized_end=703,
)


_BILLINGSCURSORRESPONSE = _descriptor.Descriptor(
  name='BillingsCursorResponse',
  full_name='api.query.webclient.v1.BillingsCursorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billingsData', full_name='api.query.webclient.v1.BillingsCursorResponse.billingsData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='api.query.webclient.v1.BillingsCursorResponse.cursor', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=705,
  serialized_end=808,
)


_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='api.query.webclient.v1.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.query.webclient.v1.Filter.key', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operand', full_name='api.query.webclient.v1.Filter.operand', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='api.query.webclient.v1.Filter.values', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=810,
  serialized_end=933,
)


_ORDERING = _descriptor.Descriptor(
  name='Ordering',
  full_name='api.query.webclient.v1.Ordering',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='api.query.webclient.v1.Ordering.key', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='api.query.webclient.v1.Ordering.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=935,
  serialized_end=1048,
)


_BILLINGSPAGINATIONREQUEST = _descriptor.Descriptor(
  name='BillingsPaginationRequest',
  full_name='api.query.webclient.v1.BillingsPaginationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cursor', full_name='api.query.webclient.v1.BillingsPaginationRequest.cursor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filters', full_name='api.query.webclient.v1.BillingsPaginationRequest.filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='api.query.webclient.v1.BillingsPaginationRequest.orders', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='api.query.webclient.v1.BillingsPaginationRequest.limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1051,
  serialized_end=1208,
)

_PROFILEDATALIST.fields_by_name['profiles'].message_type = _PROFILEDATA
_PROFILESREQUEST.fields_by_name['profilesData'].message_type = _PROFILEDATALIST
_PROFILESREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_BILLINGDATALIST.fields_by_name['billings'].message_type = _BILLINGDATA
_BILLINGSREQUEST.fields_by_name['billingsData'].message_type = _BILLINGDATALIST
_BILLINGSREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_BILLINGSCURSORRESPONSE.fields_by_name['billingsData'].message_type = _BILLINGDATALIST
_FILTER.fields_by_name['key'].enum_type = _BILLINGKEY
_FILTER.fields_by_name['operand'].enum_type = _OPERAND
_ORDERING.fields_by_name['key'].enum_type = _BILLINGKEY
_ORDERING.fields_by_name['direction'].enum_type = _DIRECTION
_BILLINGSPAGINATIONREQUEST.fields_by_name['filters'].message_type = _FILTER
_BILLINGSPAGINATIONREQUEST.fields_by_name['orders'].message_type = _ORDERING
DESCRIPTOR.message_types_by_name['ProfileData'] = _PROFILEDATA
DESCRIPTOR.message_types_by_name['ProfileDataList'] = _PROFILEDATALIST
DESCRIPTOR.message_types_by_name['ProfilesRequest'] = _PROFILESREQUEST
DESCRIPTOR.message_types_by_name['BillingData'] = _BILLINGDATA
DESCRIPTOR.message_types_by_name['BillingDataList'] = _BILLINGDATALIST
DESCRIPTOR.message_types_by_name['BillingsRequest'] = _BILLINGSREQUEST
DESCRIPTOR.message_types_by_name['BillingsCursorResponse'] = _BILLINGSCURSORRESPONSE
DESCRIPTOR.message_types_by_name['Filter'] = _FILTER
DESCRIPTOR.message_types_by_name['Ordering'] = _ORDERING
DESCRIPTOR.message_types_by_name['BillingsPaginationRequest'] = _BILLINGSPAGINATIONREQUEST
DESCRIPTOR.enum_types_by_name['BillingKey'] = _BILLINGKEY
DESCRIPTOR.enum_types_by_name['Operand'] = _OPERAND
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfileData = _reflection.GeneratedProtocolMessageType('ProfileData', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEDATA,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.ProfileData)
  })
_sym_db.RegisterMessage(ProfileData)

ProfileDataList = _reflection.GeneratedProtocolMessageType('ProfileDataList', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEDATALIST,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.ProfileDataList)
  })
_sym_db.RegisterMessage(ProfileDataList)

ProfilesRequest = _reflection.GeneratedProtocolMessageType('ProfilesRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROFILESREQUEST,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.ProfilesRequest)
  })
_sym_db.RegisterMessage(ProfilesRequest)

BillingData = _reflection.GeneratedProtocolMessageType('BillingData', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGDATA,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.BillingData)
  })
_sym_db.RegisterMessage(BillingData)

BillingDataList = _reflection.GeneratedProtocolMessageType('BillingDataList', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGDATALIST,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.BillingDataList)
  })
_sym_db.RegisterMessage(BillingDataList)

BillingsRequest = _reflection.GeneratedProtocolMessageType('BillingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGSREQUEST,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.BillingsRequest)
  })
_sym_db.RegisterMessage(BillingsRequest)

BillingsCursorResponse = _reflection.GeneratedProtocolMessageType('BillingsCursorResponse', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGSCURSORRESPONSE,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.BillingsCursorResponse)
  })
_sym_db.RegisterMessage(BillingsCursorResponse)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.Filter)
  })
_sym_db.RegisterMessage(Filter)

Ordering = _reflection.GeneratedProtocolMessageType('Ordering', (_message.Message,), {
  'DESCRIPTOR' : _ORDERING,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.Ordering)
  })
_sym_db.RegisterMessage(Ordering)

BillingsPaginationRequest = _reflection.GeneratedProtocolMessageType('BillingsPaginationRequest', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGSPAGINATIONREQUEST,
  '__module__' : 'proto.query.web_client.query_webclient_pb2'
  # @@protoc_insertion_point(class_scope:api.query.webclient.v1.BillingsPaginationRequest)
  })
_sym_db.RegisterMessage(BillingsPaginationRequest)



_PROFILE = _descriptor.ServiceDescriptor(
  name='Profile',
  full_name='api.query.webclient.v1.Profile',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1418,
  serialized_end=1595,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='api.query.webclient.v1.Profile.Get',
    index=0,
    containing_service=None,
    input_type=_PROFILESREQUEST,
    output_type=_PROFILEDATALIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Identification',
    full_name='api.query.webclient.v1.Profile.Identification',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_PROFILEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROFILE)

DESCRIPTOR.services_by_name['Profile'] = _PROFILE


_BILLING = _descriptor.ServiceDescriptor(
  name='Billing',
  full_name='api.query.webclient.v1.Billing',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1597,
  serialized_end=1695,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='api.query.webclient.v1.Billing.Get',
    index=0,
    containing_service=None,
    input_type=_BILLINGSREQUEST,
    output_type=_BILLINGDATALIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLING)

DESCRIPTOR.services_by_name['Billing'] = _BILLING


_BILLINGHISTORY = _descriptor.ServiceDescriptor(
  name='BillingHistory',
  full_name='api.query.webclient.v1.BillingHistory',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1697,
  serialized_end=1819,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='api.query.webclient.v1.BillingHistory.Get',
    index=0,
    containing_service=None,
    input_type=_BILLINGSPAGINATIONREQUEST,
    output_type=_BILLINGSCURSORRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLINGHISTORY)

DESCRIPTOR.services_by_name['BillingHistory'] = _BILLINGHISTORY

# @@protoc_insertion_point(module_scope)
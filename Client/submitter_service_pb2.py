# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: submitter_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import objects_pb2 as objects__pb2
import task_status_pb2 as task__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17submitter_service.proto\x12\x13\x41rmoniK.api.grpc.v1\x1a\robjects.proto\x1a\x11task_status.proto\"\x15\n\x07Session\x12\n\n\x02Id\x18\x01 \x01(\t\"a\n\x14\x43reateSessionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12=\n\x13\x64\x65\x66\x61ult_task_option\x18\x03 \x01(\x0b\x32 .ArmoniK.api.grpc.v1.TaskOptions\"Y\n\x12\x43reateSessionReply\x12(\n\x02Ok\x18\x01 \x01(\x0b\x32\x1a.ArmoniK.api.grpc.v1.EmptyH\x00\x12\x0f\n\x05\x45rror\x18\x02 \x01(\tH\x00\x42\x08\n\x06result\"\x9d\x01\n\x16\x43reateSmallTaskRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x36\n\x0ctask_options\x18\x02 \x01(\x0b\x32 .ArmoniK.api.grpc.v1.TaskOptions\x12\x37\n\rtask_requests\x18\x03 \x03(\x0b\x32 .ArmoniK.api.grpc.v1.TaskRequest\"\xbf\x02\n\x16\x43reateLargeTaskRequest\x12O\n\x0cinit_request\x18\x01 \x01(\x0b\x32\x37.ArmoniK.api.grpc.v1.CreateLargeTaskRequest.InitRequestH\x00\x12\x39\n\tinit_task\x18\x02 \x01(\x0b\x32$.ArmoniK.api.grpc.v1.InitTaskRequestH\x00\x12\x36\n\x0ctask_payload\x18\x03 \x01(\x0b\x32\x1e.ArmoniK.api.grpc.v1.DataChunkH\x00\x1aY\n\x0bInitRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x36\n\x0ctask_options\x18\x02 \x01(\x0b\x32 .ArmoniK.api.grpc.v1.TaskOptionsB\x06\n\x04Type\"\xd0\x03\n\nTaskFilter\x12=\n\x07session\x18\x01 \x01(\x0b\x32*.ArmoniK.api.grpc.v1.TaskFilter.IdsRequestH\x00\x12>\n\x08\x64ispatch\x18\x02 \x01(\x0b\x32*.ArmoniK.api.grpc.v1.TaskFilter.IdsRequestH\x00\x12:\n\x04task\x18\x03 \x01(\x0b\x32*.ArmoniK.api.grpc.v1.TaskFilter.IdsRequestH\x00\x12\x43\n\x08included\x18\x04 \x01(\x0b\x32/.ArmoniK.api.grpc.v1.TaskFilter.StatusesRequestH\x01\x12\x43\n\x08\x65xcluded\x18\x05 \x01(\x0b\x32/.ArmoniK.api.grpc.v1.TaskFilter.StatusesRequestH\x01\x1a\x19\n\nIdsRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1aO\n\x0fStatusesRequest\x12<\n\x08Statuses\x18\x01 \x03(\x0e\x32*.ArmoniK.api.grpc.v1.TaskStatus.TaskStatusB\x05\n\x03IdsB\n\n\x08Statuses\"#\n\x10GetStatusrequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\"L\n\x0eGetStatusReply\x12:\n\x06status\x18\x02 \x01(\x0e\x32*.ArmoniK.api.grpc.v1.TaskStatus.TaskStatus\"\x96\x01\n\x0bResultReply\x12\x30\n\x06result\x18\x01 \x01(\x0b\x32\x1e.ArmoniK.api.grpc.v1.DataChunkH\x00\x12/\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1e.ArmoniK.api.grpc.v1.TaskErrorH\x00\x12\x1c\n\x12not_completed_task\x18\x03 \x01(\tH\x00\x42\x06\n\x04Type\"\x94\x01\n\x11\x41vailabilityReply\x12(\n\x02ok\x18\x01 \x01(\x0b\x32\x1a.ArmoniK.api.grpc.v1.EmptyH\x00\x12/\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1e.ArmoniK.api.grpc.v1.TaskErrorH\x00\x12\x1c\n\x12not_completed_task\x18\x03 \x01(\tH\x00\x42\x06\n\x04Type\"\x89\x01\n\x0bWaitRequest\x12/\n\x06\x46ilter\x18\x01 \x01(\x0b\x32\x1f.ArmoniK.api.grpc.v1.TaskFilter\x12 \n\x18stop_on_first_task_error\x18\x02 \x01(\x08\x12\'\n\x1fstop_on_first_task_cancellation\x18\x03 \x01(\x08\x32\x8e\t\n\tSubmitter\x12Y\n\x17GetServiceConfiguration\x12\x1a.ArmoniK.api.grpc.v1.Empty\x1a\".ArmoniK.api.grpc.v1.Configuration\x12\x63\n\rCreateSession\x12).ArmoniK.api.grpc.v1.CreateSessionRequest\x1a\'.ArmoniK.api.grpc.v1.CreateSessionReply\x12I\n\rCancelSession\x12\x1c.ArmoniK.api.grpc.v1.Session\x1a\x1a.ArmoniK.api.grpc.v1.Empty\x12\x65\n\x10\x43reateSmallTasks\x12+.ArmoniK.api.grpc.v1.CreateSmallTaskRequest\x1a$.ArmoniK.api.grpc.v1.CreateTaskReply\x12g\n\x10\x43reateLargeTasks\x12+.ArmoniK.api.grpc.v1.CreateLargeTaskRequest\x1a$.ArmoniK.api.grpc.v1.CreateTaskReply(\x01\x12M\n\tListTasks\x12\x1f.ArmoniK.api.grpc.v1.TaskFilter\x1a\x1f.ArmoniK.api.grpc.v1.TaskIdList\x12I\n\nCountTasks\x12\x1f.ArmoniK.api.grpc.v1.TaskFilter\x1a\x1a.ArmoniK.api.grpc.v1.Count\x12\\\n\x12TryGetResultStream\x12\".ArmoniK.api.grpc.v1.ResultRequest\x1a .ArmoniK.api.grpc.v1.ResultReply0\x01\x12S\n\x10TryGetTaskOutput\x12\".ArmoniK.api.grpc.v1.ResultRequest\x1a\x1b.ArmoniK.api.grpc.v1.Output\x12\x61\n\x13WaitForAvailability\x12\".ArmoniK.api.grpc.v1.ResultRequest\x1a&.ArmoniK.api.grpc.v1.AvailabilityReply\x12Q\n\x11WaitForCompletion\x12 .ArmoniK.api.grpc.v1.WaitRequest\x1a\x1a.ArmoniK.api.grpc.v1.Count\x12J\n\x0b\x43\x61ncelTasks\x12\x1f.ArmoniK.api.grpc.v1.TaskFilter\x1a\x1a.ArmoniK.api.grpc.v1.Empty\x12W\n\tGetStatus\x12%.ArmoniK.api.grpc.v1.GetStatusrequest\x1a#.ArmoniK.api.grpc.v1.GetStatusReplyB\x16\xaa\x02\x13\x41rmoniK.Api.gRPC.V1b\x06proto3')



_SESSION = DESCRIPTOR.message_types_by_name['Session']
_CREATESESSIONREQUEST = DESCRIPTOR.message_types_by_name['CreateSessionRequest']
_CREATESESSIONREPLY = DESCRIPTOR.message_types_by_name['CreateSessionReply']
_CREATESMALLTASKREQUEST = DESCRIPTOR.message_types_by_name['CreateSmallTaskRequest']
_CREATELARGETASKREQUEST = DESCRIPTOR.message_types_by_name['CreateLargeTaskRequest']
_CREATELARGETASKREQUEST_INITREQUEST = _CREATELARGETASKREQUEST.nested_types_by_name['InitRequest']
_TASKFILTER = DESCRIPTOR.message_types_by_name['TaskFilter']
_TASKFILTER_IDSREQUEST = _TASKFILTER.nested_types_by_name['IdsRequest']
_TASKFILTER_STATUSESREQUEST = _TASKFILTER.nested_types_by_name['StatusesRequest']
_GETSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetStatusrequest']
_GETSTATUSREPLY = DESCRIPTOR.message_types_by_name['GetStatusReply']
_RESULTREPLY = DESCRIPTOR.message_types_by_name['ResultReply']
_AVAILABILITYREPLY = DESCRIPTOR.message_types_by_name['AvailabilityReply']
_WAITREQUEST = DESCRIPTOR.message_types_by_name['WaitRequest']
Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.Session)
  })
_sym_db.RegisterMessage(Session)

CreateSessionRequest = _reflection.GeneratedProtocolMessageType('CreateSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESESSIONREQUEST,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.CreateSessionRequest)
  })
_sym_db.RegisterMessage(CreateSessionRequest)

CreateSessionReply = _reflection.GeneratedProtocolMessageType('CreateSessionReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATESESSIONREPLY,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.CreateSessionReply)
  })
_sym_db.RegisterMessage(CreateSessionReply)

CreateSmallTaskRequest = _reflection.GeneratedProtocolMessageType('CreateSmallTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESMALLTASKREQUEST,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.CreateSmallTaskRequest)
  })
_sym_db.RegisterMessage(CreateSmallTaskRequest)

CreateLargeTaskRequest = _reflection.GeneratedProtocolMessageType('CreateLargeTaskRequest', (_message.Message,), {

  'InitRequest' : _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), {
    'DESCRIPTOR' : _CREATELARGETASKREQUEST_INITREQUEST,
    '__module__' : 'submitter_service_pb2'
    # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.CreateLargeTaskRequest.InitRequest)
    })
  ,
  'DESCRIPTOR' : _CREATELARGETASKREQUEST,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.CreateLargeTaskRequest)
  })
_sym_db.RegisterMessage(CreateLargeTaskRequest)
_sym_db.RegisterMessage(CreateLargeTaskRequest.InitRequest)

TaskFilter = _reflection.GeneratedProtocolMessageType('TaskFilter', (_message.Message,), {

  'IdsRequest' : _reflection.GeneratedProtocolMessageType('IdsRequest', (_message.Message,), {
    'DESCRIPTOR' : _TASKFILTER_IDSREQUEST,
    '__module__' : 'submitter_service_pb2'
    # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.TaskFilter.IdsRequest)
    })
  ,

  'StatusesRequest' : _reflection.GeneratedProtocolMessageType('StatusesRequest', (_message.Message,), {
    'DESCRIPTOR' : _TASKFILTER_STATUSESREQUEST,
    '__module__' : 'submitter_service_pb2'
    # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.TaskFilter.StatusesRequest)
    })
  ,
  'DESCRIPTOR' : _TASKFILTER,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.TaskFilter)
  })
_sym_db.RegisterMessage(TaskFilter)
_sym_db.RegisterMessage(TaskFilter.IdsRequest)
_sym_db.RegisterMessage(TaskFilter.StatusesRequest)

GetStatusrequest = _reflection.GeneratedProtocolMessageType('GetStatusrequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSREQUEST,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.GetStatusrequest)
  })
_sym_db.RegisterMessage(GetStatusrequest)

GetStatusReply = _reflection.GeneratedProtocolMessageType('GetStatusReply', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSREPLY,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.GetStatusReply)
  })
_sym_db.RegisterMessage(GetStatusReply)

ResultReply = _reflection.GeneratedProtocolMessageType('ResultReply', (_message.Message,), {
  'DESCRIPTOR' : _RESULTREPLY,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.ResultReply)
  })
_sym_db.RegisterMessage(ResultReply)

AvailabilityReply = _reflection.GeneratedProtocolMessageType('AvailabilityReply', (_message.Message,), {
  'DESCRIPTOR' : _AVAILABILITYREPLY,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.AvailabilityReply)
  })
_sym_db.RegisterMessage(AvailabilityReply)

WaitRequest = _reflection.GeneratedProtocolMessageType('WaitRequest', (_message.Message,), {
  'DESCRIPTOR' : _WAITREQUEST,
  '__module__' : 'submitter_service_pb2'
  # @@protoc_insertion_point(class_scope:ArmoniK.api.grpc.v1.WaitRequest)
  })
_sym_db.RegisterMessage(WaitRequest)

_SUBMITTER = DESCRIPTOR.services_by_name['Submitter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\023ArmoniK.Api.gRPC.V1'
  _SESSION._serialized_start=82
  _SESSION._serialized_end=103
  _CREATESESSIONREQUEST._serialized_start=105
  _CREATESESSIONREQUEST._serialized_end=202
  _CREATESESSIONREPLY._serialized_start=204
  _CREATESESSIONREPLY._serialized_end=293
  _CREATESMALLTASKREQUEST._serialized_start=296
  _CREATESMALLTASKREQUEST._serialized_end=453
  _CREATELARGETASKREQUEST._serialized_start=456
  _CREATELARGETASKREQUEST._serialized_end=775
  _CREATELARGETASKREQUEST_INITREQUEST._serialized_start=678
  _CREATELARGETASKREQUEST_INITREQUEST._serialized_end=767
  _TASKFILTER._serialized_start=778
  _TASKFILTER._serialized_end=1242
  _TASKFILTER_IDSREQUEST._serialized_start=1117
  _TASKFILTER_IDSREQUEST._serialized_end=1142
  _TASKFILTER_STATUSESREQUEST._serialized_start=1144
  _TASKFILTER_STATUSESREQUEST._serialized_end=1223
  _GETSTATUSREQUEST._serialized_start=1244
  _GETSTATUSREQUEST._serialized_end=1279
  _GETSTATUSREPLY._serialized_start=1281
  _GETSTATUSREPLY._serialized_end=1357
  _RESULTREPLY._serialized_start=1360
  _RESULTREPLY._serialized_end=1510
  _AVAILABILITYREPLY._serialized_start=1513
  _AVAILABILITYREPLY._serialized_end=1661
  _WAITREQUEST._serialized_start=1664
  _WAITREQUEST._serialized_end=1801
  _SUBMITTER._serialized_start=1804
  _SUBMITTER._serialized_end=2970
# @@protoc_insertion_point(module_scope)

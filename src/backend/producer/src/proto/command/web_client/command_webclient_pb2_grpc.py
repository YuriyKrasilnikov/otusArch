# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.command.web_client import command_webclient_pb2 as proto_dot_command_dot_web__client_dot_command__webclient__pb2


class ProfileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Insert = channel.unary_stream(
                '/api.command.webclient.v1.Profile/Insert',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.SerializeToString,
                response_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
                )
        self.Update = channel.unary_stream(
                '/api.command.webclient.v1.Profile/Update',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.SerializeToString,
                response_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
                )
        self.Remove = channel.unary_stream(
                '/api.command.webclient.v1.Profile/Remove',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.SerializeToString,
                response_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
                )


class ProfileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Insert': grpc.unary_stream_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.FromString,
                    response_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.SerializeToString,
            ),
            'Update': grpc.unary_stream_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.FromString,
                    response_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.SerializeToString,
            ),
            'Remove': grpc.unary_stream_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.FromString,
                    response_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.command.webclient.v1.Profile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Profile(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.command.webclient.v1.Profile/Insert',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.SerializeToString,
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.command.webclient.v1.Profile/Update',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.SerializeToString,
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.command.webclient.v1.Profile/Remove',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.ProfileData.SerializeToString,
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BillingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Paid = channel.unary_stream(
                '/api.command.webclient.v1.Billing/Paid',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.PaidData.SerializeToString,
                response_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
                )
        self.Buy = channel.unary_stream(
                '/api.command.webclient.v1.Billing/Buy',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.BuyData.SerializeToString,
                response_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
                )


class BillingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Paid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Buy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BillingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Paid': grpc.unary_stream_rpc_method_handler(
                    servicer.Paid,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.PaidData.FromString,
                    response_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.SerializeToString,
            ),
            'Buy': grpc.unary_stream_rpc_method_handler(
                    servicer.Buy,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.BuyData.FromString,
                    response_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.command.webclient.v1.Billing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Billing(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Paid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.command.webclient.v1.Billing/Paid',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.PaidData.SerializeToString,
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Buy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.command.webclient.v1.Billing/Buy',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.BuyData.SerializeToString,
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ChartsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InsertNodes = channel.unary_unary(
                '/api.command.webclient.v1.Charts/InsertNodes',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateNodes = channel.unary_unary(
                '/api.command.webclient.v1.Charts/UpdateNodes',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RemoveNodes = channel.unary_unary(
                '/api.command.webclient.v1.Charts/RemoveNodes',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.InsertEdges = channel.unary_unary(
                '/api.command.webclient.v1.Charts/InsertEdges',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateEdges = channel.unary_unary(
                '/api.command.webclient.v1.Charts/UpdateEdges',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RemoveEdges = channel.unary_unary(
                '/api.command.webclient.v1.Charts/RemoveEdges',
                request_serializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ChartsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InsertNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertEdges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEdges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveEdges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChartsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InsertNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertNodes,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNodes,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RemoveNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveNodes,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'InsertEdges': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertEdges,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateEdges': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEdges,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RemoveEdges': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveEdges,
                    request_deserializer=proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.command.webclient.v1.Charts', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Charts(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InsertNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.command.webclient.v1.Charts/InsertNodes',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.command.webclient.v1.Charts/UpdateNodes',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.command.webclient.v1.Charts/RemoveNodes',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.NodesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertEdges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.command.webclient.v1.Charts/InsertEdges',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEdges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.command.webclient.v1.Charts/UpdateEdges',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveEdges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.command.webclient.v1.Charts/RemoveEdges',
            proto_dot_command_dot_web__client_dot_command__webclient__pb2.EdgesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

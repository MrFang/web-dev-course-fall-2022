import os

import app.proto.messages_pb2 as messages
import app.proto.services_pb2_grpc as services
from utils import get_files_with_content


class AssetServicer(services.AssetServiceServicer):
    def __init__(self, content_root: str) -> None:
        """ Inits servicer with given content root

        Args:
            content_root (str): absolute path to directory \
                from which all requested dirs will be resolved
        """
        super().__init__()

        assert os.path.isabs(content_root)
        assert os.path.isdir(content_root)

        # remove trailing slash
        self.__content_root = os.path.dirname(content_root)

    def GetAll(self, request: messages.Directory, context) -> messages.Assets:
        """ Returns list of files with their content in given directory

        Args:
            request (app.proto.messages_pb2.Directory): directory with files
            context (Any): not used

        Returns:
            messages.Assets: files with content
        """
        return messages.Assets(asset=[
            messages.Asset(name=name, data=data)
            for name, data in get_files_with_content(
                os.path.join(self.__content_root, request.directory)).items()
        ])

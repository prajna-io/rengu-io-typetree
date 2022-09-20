from uuid import UUID

from rengu.io import RenguOutput, with_templating

import typetree

class RenguOutputTypetree(RenguOutput):

    @with_templating
    def __call__(self, obj: UUID | dict):
        
        tree = typetree.Tree(obj)

        print(tree.to_string(obj), file=self.fd, flush=True)


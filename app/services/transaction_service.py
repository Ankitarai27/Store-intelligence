class TransactionService:
    def __init__(self, visitor_repo):
        self.visitor_repo = visitor_repo

    def mark_converted(self, visitor_id):
        visitor = self.visitor_repo.get(visitor_id)
        if visitor:
            visitor.is_converted = True
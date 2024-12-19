from infraestructure.repository.dto.history import History


class HistoryRepository:
    def add_history(self, history: History) -> bool:
        return True

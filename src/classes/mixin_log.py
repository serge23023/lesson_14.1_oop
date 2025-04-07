class MixinCreationLogger:
    def log_creation(self):
        print(f"Создан объект: {self.__repr__()}\n")

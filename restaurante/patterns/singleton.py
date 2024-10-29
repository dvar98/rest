# patterns/singleton.py
class ConfiguracionGlobal:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfiguracionGlobal, cls).__new__(cls)
            cls._instance.parametros = {}
        return cls._instance

    def set_parametro(self, clave, valor):
        self.parametros[clave] = valor

    def get_parametro(self, clave):
        return self.parametros.get(clave)
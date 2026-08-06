import requests
import time
from datetime import datetime


class EndpointAuditor:
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "PokeAPI-Health-Auditor/1.0"
        })

    def auditar(self, url: str, campos_obligatorios: list[str] = None):
        resultado = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "status_code": None,
            "latencia_ms": None,
            "ok": False,
            "error": None,
            "campos_validados": None
        }

        try:
            inicio = time.perf_counter()
            response = self.session.get(url, timeout=self.timeout)
            fin = time.perf_counter()

            resultado["latencia_ms"] = round((fin - inicio) * 1000, 2)
            resultado["status_code"] = response.status_code

            if response.status_code != 200:
                resultado["error"] = f"HTTP {response.status_code}"
                return resultado

            data = response.json()

            if campos_obligatorios:
                faltantes = [c for c in campos_obligatorios if c not in data]
                if faltantes:
                    resultado["error"] = f"Campos faltantes: {faltantes}"
                    return resultado
                resultado["campos_validados"] = campos_obligatorios

            resultado["ok"] = True

        except requests.exceptions.Timeout:
            resultado["error"] = f"Timeout después de {self.timeout}s"
        except requests.exceptions.ConnectionError:
            resultado["error"] = "Error de conexión"
        except requests.exceptions.HTTPError as e:
            resultado["error"] = f"HTTP Error: {e}"
        except ValueError:
            resultado["error"] = "Respuesta no es JSON válido"
        except Exception as e:
            resultado["error"] = f"Error inesperado: {e}"

        return resultado



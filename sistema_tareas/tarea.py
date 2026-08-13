from dataclasses import dataclass

PRIORIDADES = {1: "alta", 2: "media", 3: "baja"}
ESTADOS = ("pendiente", "en_progreso", "completada")


@dataclass
class Tarea:
    id: int
    descripcion: str
    prioridad: int  # 1 = alta, 2 = media, 3 = baja
    tiempo: float  # valor numerico para desempatar/ordenar (p.ej. dias restantes)
    estado: str = "pendiente"

    def __str__(self) -> str:
        nombre_prioridad = PRIORIDADES.get(self.prioridad, "?")
        return (
            f"[{self.id}] {self.descripcion} "
            f"(prioridad={self.prioridad}/{nombre_prioridad}, "
            f"tiempo={self.tiempo}, estado={self.estado})"
        )

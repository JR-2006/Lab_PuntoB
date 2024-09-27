from datetime import datetime

tareas = [
    {'nombre': 'Tarea 1', 'dias_asignados': 10},
    {'nombre': 'Tarea 2', 'dias_asignados': 5},
    {'nombre': 'Tarea 3', 'dias_asignados': 15},
]

for tarea in tareas:
    fecha_limite = input(f"Ingrese la fecha límite para {tarea['nombre']} (AAAA-MM-DD): ")
    fecha_completada = input(f"Ingrese la fecha de completado para {tarea['nombre']} (AAAA-MM-DD): ")
    
    fecha_limite_dt = datetime.strptime(fecha_limite, '%Y-%m-%d')
    fecha_completada_dt = datetime.strptime(fecha_completada, '%Y-%m-%d')
    
    dias_retraso = max((fecha_completada_dt - fecha_limite_dt).days, 0)
    dias_asignados = tarea['dias_asignados']
    
    if dias_asignados:
        porcentaje_retraso = (dias_retraso / dias_asignados) * 100
    else:
        porcentaje_retraso = 0
    
    print(f"{tarea['nombre']}: {dias_retraso} días de retraso, {porcentaje_retraso:.2f}% de retraso")


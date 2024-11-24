def maxArea(height):
    izq, der = 0, len(height) - 1
    max_area = 0
    
    while izq < der:
        # Calcular el área actual
        altura = min(height[izq], height[der])
        ancho = der - izq
        area = altura * ancho
        # Actualizar el área máxima
        max_area = max(max_area, area)
        
        # Mover el puntero menor
        if height[izq] < height[der]:
            izq += 1
        else:
            der -= 1
    
    return max_area


height = [1, 2,3, 4,7]
print("El área máxima es:", maxArea(height))

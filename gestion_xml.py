import xml.etree.ElementTree as ET

# Cargar el archivo XML
tree = ET.parse('archivo_prueba.xml')
root = tree.getroot()

# Recorrer los elementos del XML
for libro in root.findall('libro'):
    id = libro.get('id')
    titulo = libro.find('titulo').text
    autor = libro.find('autor').text
    año = libro.find('año').text
    print(f"ID: {id}, Título: {titulo}, Autor: {autor}, Año: {año}")

# Añadir un nuevo libro
nuevo_libro = ET.Element('libro', id='4')
nuevo_titulo = ET.SubElement(nuevo_libro, 'titulo')
nuevo_titulo.text = 'El Hobbit'
nuevo_autor = ET.SubElement(nuevo_libro, 'autor')
nuevo_autor.text = 'J.R.R. Tolkien'
nuevo_año = ET.SubElement(nuevo_libro, 'año')
nuevo_año.text = '1937'
root.append(nuevo_libro)

# Guardar los cambios en un nuevo archivo XML
tree.write('archivo_prueba_actualizado.xml', encoding='UTF-8', xml_declaration=True)

print("\nSe ha añadido un nuevo libro y se ha guardado en 'archivo_prueba_actualizado.xml'")

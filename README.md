Documentación de la API de Catálogo de Películas 🎬
1. Endpoint para Crear una Película
URL: /api/movies/

Método HTTP: POST

Parámetros requeridos:

title: Título de la película (String).

description: Descripción de la película (String).

release_date: Fecha de estreno (Formato YYYY-MM-DD).

director: ID del director (Integer).

actors: Lista de IDs de actores (Array de Integer).

genres: Lista de IDs de géneros (Array de Integer).

Parámetros opcionales: Ninguno.

Formato de respuesta:

Éxito (201 Created):

json
Copiar
{
  "id": 1,
  "title": "Juan el caballo",
  "description": "Una historia sobre caballos",
  "release_date": "2025-01-01",
  "director": 1,
  "actors": [1, 2],
  "genres": [1, 2]
}
Códigos de estado:

201 Created: La película fue creada con éxito.

400 Bad Request: Si algún campo es inválido o falta un campo requerido.

2. Endpoint para Obtener una Lista de Películas
URL: /api/movies/

Método HTTP: GET

Parámetros requeridos: Ninguno.

Parámetros opcionales:

query: Búsqueda de películas por título (String, opcional).

Formato de respuesta:

Éxito (200 OK):

json
Copiar
[
  {
    "id": 1,
    "title": "Juan el caballo",
    "description": "Una historia sobre caballos",
    "release_date": "2025-01-01",
    "director": 1,
    "actors": [1, 2],
    "genres": [1, 2]
  },
  {
    "id": 2,
    "title": "Aventura en la selva",
    "description": "Una historia en la selva",
    "release_date": "2024-06-15",
    "director": 2,
    "actors": [2, 3],
    "genres": [2]
  }
]
Códigos de estado:

200 OK: La lista de películas se ha recuperado correctamente.

3. Endpoint para Obtener los Detalles de una Película
URL: /api/movies/{id}/

Método HTTP: GET

Parámetros requeridos:

id: ID de la película (Integer).

Parámetros opcionales: Ninguno.

Formato de respuesta:

Éxito (200 OK):

json
Copiar
{
  "id": 1,
  "title": "Juan el caballo",
  "description": "Una historia sobre caballos",
  "release_date": "2025-01-01",
  "director": 1,
  "actors": [
    {"id": 1, "name": "Actor 1", "bio": "Actor 1 bio"},
    {"id": 2, "name": "Actor 2", "bio": "Actor 2 bio"}
  ],
  "genres": [
    {"id": 1, "name": "Acción", "description": "Acción épica"},
    {"id": 2, "name": "Aventura", "description": "Aventura emocionante"}
  ],
  "reviews": [
    {
      "id": 1,
      "user": "User 1",
      "rating": 5,
      "content": "¡Excelente película!",
      "created_at": "2025-05-01T12:00:00Z"
    }
  ]
}
Códigos de estado:

200 OK: Los detalles de la película se han recuperado correctamente.

404 Not Found: Si la película con el ID especificado no existe.

4. Endpoint para Crear una Reseña de una Película
URL: /api/movies/{id}/reviews/

Método HTTP: POST

Parámetros requeridos:

movie: ID de la película (Integer).

user: Nombre del usuario que realiza la reseña (String).

rating: Calificación de la película (Integer entre 1 y 5).

content: Contenido de la reseña (String).

Parámetros opcionales: Ninguno.

Formato de respuesta:

Éxito (201 Created):

json
Copiar
{
  "id": 1,
  "movie": 1,
  "user": "User 1",
  "rating": 5,
  "content": "¡Excelente película!",
  "created_at": "2025-05-01T12:00:00Z"
}
Códigos de estado:

201 Created: La reseña fue creada con éxito.

400 Bad Request: Si algún campo es inválido o falta un campo requerido.

5. Endpoint para Buscar Películas
URL: /api/movies/search/

Método HTTP: GET

Parámetros requeridos:

query: Palabra clave para buscar películas (String).

Parámetros opcionales: Ninguno.

Formato de respuesta:

Éxito (200 OK):

json
Copiar
[
  {
    "id": 1,
    "title": "Juan el caballo",
    "description": "Una historia sobre caballos",
    "release_date": "2025-01-01",
    "director": 1,
    "actors": [1, 2],
    "genres": [1, 2]
  }
]
Códigos de estado:

200 OK: La búsqueda se ha realizado correctamente y se ha encontrado al menos una película.

404 Not Found: Si no se encuentran resultados.

6. Endpoint para Agregar una Película a la Lista de Favoritas
URL: /api/movies/add_favorite/

Método HTTP: POST

Parámetros requeridos:

movie_id: ID de la película a agregar a la lista de favoritos (Integer).

Nota: Este endpoint requiere autenticación de usuario (implementación adicional).

Parámetros opcionales: Ninguno.

Formato de respuesta:

Éxito (200 OK):

json
Copiar
{
  "message": "Película agregada a tus favoritos",
  "movie_id": 1
}
Códigos de estado:

200 OK: La película fue agregada a la lista de favoritos correctamente.

401 Unauthorized: Si no estás autenticado correctamente.

7. Endpoint para Obtener la Lista de Películas Favoritas
URL: /api/movies/favorites/

Método HTTP: GET

Parámetros requeridos: Ninguno.

Parámetros opcionales: Ninguno.

Formato de respuesta:

Éxito (200 OK):

json
Copiar
[
  {
    "id": 1,
    "title": "Juan el caballo",
    "description": "Una historia sobre caballos",
    "release_date": "2025-01-01",
    "director": 1,
    "actors": [1, 2],
    "genres": [1, 2]
  }
]
Códigos de estado:

200 OK: La lista de favoritos se ha recuperado correctamente.

401 Unauthorized: Si no estás autenticado correctamente.

Códigos de Estado Comunes:
200 OK: La solicitud se procesó correctamente.

201 Created: El recurso fue creado correctamente (por ejemplo, al crear una película o una reseña).

400 Bad Request: La solicitud está mal formada o le faltan datos.

401 Unauthorized: Se requiere autenticación para acceder al recurso.

404 Not Found: El recurso solicitado no se encuentra.

500 Internal Server Error: Un error interno ocurrió en el servidor.

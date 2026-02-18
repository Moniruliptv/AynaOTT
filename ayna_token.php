<?php
header('Content-Type: application/json; charset=UTF-8');
echo <<<JSON
{
    "code": 1,
    "message": "Success",
    "content": {
        "user_id": "78be6644-0a65-48ec-81a4-089ac65a2619",
        "operatorId": "1fb1b4c7-dbd9-469e-88a2-c207dc195869",
        "status": 1,
        "token": {
            "expires_in": 43200,
            "token_type": "Bearer",
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzhiZTY2NDQtMGE2NS00OGVjLTgxYTQtMDg5YWM2NWEyNjE5Iiwib3BlcmF0b3JJZCI6IjFmYjFiNGM3LWRiZDktNDY5ZS04OGEyLWMyMDdkYzE5NTg2OSIsImdlb0lwUnVsZXMiOnsiZDE3MjUwYTMtMzk4NS00OWJjLWFlOGMtZmU3Y2JiNjA0MDhjIjp0cnVlfSwiZ2VvTG9jYXRpb24iOnsiY291bnRyeSI6IkJEIiwiY2l0eSI6IkZhcsSrZHB1ciIsImlwIjoiMTYzLjIyNy4xNDQuMTc2In0sImRldmljZUlkIjoiNTgyQ0M3ODhEMjUwQ0ZBRENBMUI2OTREODY4Mjg4QTcifSwiaWF0IjoxNzcxMzkzOTE4LCJleHAiOjE3NzE0MzcxMTh9.ILw5fJnhDYxISSN4tybminJzt8_K1DXx-7hn6ExqB6A",
            "refresh_token": "1HGL3q4oB1psMZH5iPsvXoix1jULeLZKqM0BNvapdRJsknfCFHY0bcoTqJepivJF84aBtL9EYroUsmZEscGuXHtpDaO1Hp8a3SurGvTL3Rg6bm3R1o0FWJVUytI4k9efkGv3tNPnkU6UEfLJbJ4nYu6JRriqpJUkKLCDKxZZ2vDHcneLv3AOOspL6Ha3GDo6NnNUsUoYLWRPt7d3nyWd58WMIomI9OqFakYL6LYnOE39nfIid0t6wo6IeGBIUVTo"
        }
    },
    "execTime": 259
}
JSON;

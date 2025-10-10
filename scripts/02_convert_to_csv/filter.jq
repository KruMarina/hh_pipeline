["id", "created_at", "name", "has_test", "alternate_url"] as $headers
| $headers,
(.items[] | [.[$headers[]]])
| @csv


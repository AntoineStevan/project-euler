# project-euler

My solutions for the challenges of the [Project Euler](https://projecteuler.net)

Some additional resources can be found in [`res/`](res).

## the solutions
- `python` solutions are available in [`python/`](python)

### generate language `README`s
one can run the following in `nushell`
```bash
let language = "..."

ls $language
| where name =~ \d
| select name
| upsert file {|it|
  $it.name | parse "python/{name}" | get name.0
}
| upsert id {|it|
  $it.name | parse "python/{id}.py" | get id.0 | into int
}
| upsert problem {|it|
  $"https://projecteuler.net/problem=($it.id)"
}
| reject name id
| to md --pretty
| save --force ($language | path join README.md)
```

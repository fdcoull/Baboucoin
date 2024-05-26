def strip() :
    key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDSAaPPDd5djS1O9gemQMK5KKA5djfrlov+AH5dhq/nNl7EyRei\no7O75J/HRAJF/P+LuBJdYZxHplZ65dR+a4h0uLKumbhqOMEzoR1nTeRMqalFICQI\nOiFP6wDvP+kaJmSCBlnqeA/FHmUA6QNkiO8TfY3VkTYZT5d54cF4HumzuQIDAQAB\nAoGAFflGs/u0IpcK8H4JER3p2hCsijKq2X9iRMi1sDDPf0qGukG9075cCDsc9k9R\nCxR0w0B2iHeWD/+xQREDDdrP11EQJUOwz6xqC9VvQso8Zm2dTDjkLcR3VUcUhRRG\nqC3wErAsZnbKpSnytT3S4hPGFnfd6gpmzxDGHDQ1aZn60qECQQDWfqq41tbtBotn\noaCDmwlzBOjfehe8Jw+y06mSBOLAMphYBk1lVv5/QOwdf7w4olYNU6mzGgHbDJj+\n7qdZN96hAkEA+qSiP0gkFtN4ElGRo4YTNWIKl0mJlLHsxE9xmUZ9dWhe9bT3PwpK\nx0JQKT7sal67/lOpzNvNZ2xMtmTcah82GQJAL02N7ueKTIl18uvFD2EAi3oYtTgi\nxd7DaoedTNOBAivmRvtU1DWEOKIjsDm8U60RVy0NLq9cm2dC0m3lQBq/IQJBAItq\npC0bDaf8vN9DrAUPgQPCoy1/5B1n0tFnd0LQ6Nwz0A5QOO9B5FJt2nT24T5Rr7RK\nCTtAUELlBM63z7rf3ZECQQC2zUmJGM5dmgQYJ/praCVBWM4XffpRbk0qU6U7ZsZk\nelpAjHHO9AedlnAaV5S8YnGzUmZF8B2flZXnGSXwiXaS\n-----END RSA PRIVATE KEY-----'

    stripped = key.replace(b'-----BEGIN RSA PRIVATE KEY-----', b'')
    stripped = stripped.replace(b'\n', b'')
    stripped = stripped.replace(b'-----END RSA PRIVATE KEY-----', b'')

    print(stripped)

strip()
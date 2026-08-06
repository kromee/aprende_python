from auditor import EndpointAuditor


auditor = EndpointAuditor(timeout=5)

endpoints = [
    {
        "url": "https://pokeapi.co/api/v2/pokemon/pikachu",
        "campos": ["name", "id", "types", "stats"]
    },
    {
        "url": "https://pokeapi.co/api/v2/type/fire",
        "campos": ["name", "id", "pokemon"]
    },
    {
        "url": "https://pokeapi.co/api/v2/ability/limber",
        "campos": ["name", "id", "effect_entries"]
    },
    {
        "url": "https://pokeapi.co/api/v2/pokemon/este-no-existe",
        "campos": ["name"]
    },
    {
        "url": "https://pokeapi.co/api/v2/pokemon?limit=5",
        "campos": ["count", "results"]
    }
]

print("=" * 60)
print("🔍 POKEAPI HEALTH AUDITOR")
print("=" * 60)


for ep in endpoints:
    r = auditor.auditar(ep["url"], ep.get("campos"))
    status = "✅ OK" if r["ok"] else "❌ FAIL"
    print(f"\n{status} {r['url']}")
    print(f"   Status: {r['status_code']} | Latencia: {r['latencia_ms']}ms")
    
    if r['campos_validados']:
        print(f"   Campos: {', '.join(r['campos_validados'])}")
    
    if r['error']:
        print(f"   Error: {r['error']}")
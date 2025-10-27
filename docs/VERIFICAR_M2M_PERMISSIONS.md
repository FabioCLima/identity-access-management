# ⚠️ Erro de Autorização - Machine to Machine Application

## Problema

O erro "access_denied" indica que a Machine to Machine Application não tem as permissões corretas na Management API.

---

## ✅ Solução: Autorizar Machine to Machine Application

### 1. Abrir Auth0 Dashboard

https://manage.auth0.com

### 2. Ir para Applications

- Applications → Applications
- Procurar: "Coffee Shop API (Test Application)" (Machine to Machine)

### 3. Abrir APIs Tab

Na página da Application:
- Clicar em "APIs" tab

### 4. Autorizar Management API

Você deve ver:
```
┌─────────────────────────────────────┐
│ Authorized APIs                     │
├─────────────────────────────────────┤
│ Management API                      │
│   [×] View users                    │
│   [×] Update users                  │
│   [×] Create users                  │
│   [×] Delete users                   │
│   [×] Update roles                  │
└─────────────────────────────────────┘
```

**Selecione TODAS as permissões necessárias:**

✅ Expand user details
✅ Read user attributes
✅ Create users
✅ Update users
✅ Delete users
✅ Update roles
✅ Update application grants
✅ Create roles
✅ Update roles
✅ Delete roles
✅ Read roles

### 5. Salvar

- Clicar em "Update"

### 6. Tentar novamente

```bash
cd /home/fabiolima/Workdir/udacity_projects/identity-access-management/coffee-shop
./criar_usuarios.sh
```

---

## 🔍 Verificar se M2M tem Permissões

### No Auth0 Dashboard:

1. **Applications** → "Coffee Shop API (Test Application)"
2. **APIs** tab → ver se "Management API" aparece
3. Se não aparecer → clicar em "Authorize"
4. Selecionar todas as permissões listadas acima

---

## 📝 Checklist

- [ ] M2M Application existe
- [ ] M2M está autorizada para Management API
- [ ] Todas as permissões de Users estão selecionadas
- [ ] Todas as permissões de Roles estão selecionadas
- [ ] "Update" foi clicado
- [ ] Aguardado 1 minuto
- [ ] Script executado novamente

---

## ✅ Após Configurar

O script deve funcionar corretamente e criar:
- ✅ Usuário Barista
- ✅ Usuário Manager
- ✅ Roles
- ✅ Permissions
- ✅ Atribuição de roles


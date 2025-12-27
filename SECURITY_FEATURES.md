# 🔐 Autenticação e Segurança - Hospital de Malanje

## ✅ Recursos de Segurança Implementados

### 1. **Autenticação Segura**
- ✓ Login com validação de credenciais
- ✓ Logout com limpeza de sessão
- ✓ Proteção contra força bruta (5 tentativas = bloqueio 15 min)
- ✓ Rastreamento de IP e User-Agent em todas as tentativas

### 2. **Controle de Acesso (RBAC)**
- ✓ 3 Perfis de Utilizadores: Administrador, Médico, Atendente
- ✓ Decoradores `@role_required` para proteger views
- ✓ Sistema de permissões granular por role

### 3. **Proteção de Sessão**
- ✓ `SESSION_COOKIE_HTTPONLY = True` (protege contra XSS)
- ✓ `SESSION_COOKIE_SAMESITE = 'Strict'` (CSRF protection)
- ✓ Expiração de sessão em 30 minutos de inatividade
- ✓ Cookies secure em HTTPS

### 4. **Headers de Segurança**
- ✓ `X-Content-Type-Options: nosniff` (previne MIME-sniffing)
- ✓ `X-Frame-Options: DENY` (previne clickjacking)
- ✓ `X-XSS-Protection: 1; mode=block` (protege contra XSS)
- ✓ `Referrer-Policy: strict-origin-when-cross-origin`
- ✓ `Content-Security-Policy` ativo

### 5. **Validação de Senha**
- ✓ Validação de complexidade mínima (8 caracteres)
- ✓ Protege contra senhas comuns
- ✓ Protege contra senhas iguais aos dados de utilizador
- ✓ Proteção contra senhas numéricas

### 6. **Rastreamento e Auditoria**
- ✓ **LoginAttempt**: Registra todas as tentativas (sucesso/falha)
- ✓ **ActivityLog**: Registra ações no sistema (CREATE, UPDATE, DELETE)
- ✓ IP Address + User-Agent em cada registro
- ✓ Dados indexados para consultas rápidas

### 7. **Bloqueio de Conta**
- ✓ Bloqueio automático após 5 tentativas falhadas
- ✓ Desbloqueio automático após 15 minutos
- ✓ Contador de tentativas resetado no login bem-sucedido

### 8. **CSRF Protection**
- ✓ Tokens CSRF em todos os formulários
- ✓ Validação automática em POST/PUT/DELETE
- ✓ Trusted origins configurados para Replit

---

## 📊 Modelos de Segurança

### UserProfile
```
- failed_login_attempts: Contador de falhas
- locked_until: Data/hora de desbloqueio
- last_login_ip: IP do último login
- last_login_time: Hora do último login
- password_changed_at: Quando senha foi alterada
```

### LoginAttempt
```
- username: Utilizador que tentou fazer login
- ip_address: IP da tentativa
- user_agent: Navegador/dispositivo
- success: Se login foi bem-sucedido
- timestamp: Quando ocorreu
```

### ActivityLog
```
- user: Utilizador que executou ação
- action: Tipo de ação (VIEW, CREATE, UPDATE, DELETE, etc)
- resource: Recurso afetado
- ip_address: IP do utilizador
- user_agent: Navegador/dispositivo
- details: Detalhes adicionais
- timestamp: Quando ocorreu
```

---

## 🧪 Testes de Segurança

### Tentativas de Login Brutas
```bash
# Teste: 5 tentativas com senha errada = conta bloqueada
username: doctor
password: errado (5x)
Resultado: Conta bloqueada por 15 minutos
```

### Proteção XSS
```bash
# Os formulários estão protegidos contra XSS
# - Content-Security-Policy ativo
# - X-XSS-Protection ativo
# - Sanitização automática de entrada
```

### CSRF Protection
```bash
# Todos os formulários requerem token CSRF válido
# Django valida automaticamente
```

---

## 👥 Credenciais de Teste

| Utilizador | Senha | Perfil |
|-----------|-------|--------|
| admin | admin123 | Administrador |
| doctor | doctor123 | Médico |
| receptionist | receptionist123 | Atendente |

---

## 🚀 Próximos Passos (Opcional)

1. **Autenticação Multi-Factor (2FA)**
2. **Password Reset via Email**
3. **Integração com LDAP/Active Directory**
4. **Rate Limiting por IP**
5. **Backup e Recovery Automático**

---

## 📝 Logs Disponíveis

Aceda ao Admin Panel para visualizar:
- **Tentativas de Login**: `/admin/auth_system/loginattempt/`
- **Logs de Atividade**: `/admin/auth_system/activitylog/`
- **Perfis de Utilizadores**: `/admin/auth_system/userprofile/`

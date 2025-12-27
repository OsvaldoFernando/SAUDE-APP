# 🏥 Guia do Painel Administrativo - Hospital de Malanje

## 🚀 Acesso ao Admin

**URL:** `/admin/`

**Credenciais Padrão:**
- Utilizador: `admin`
- Senha: `admin123`

---

## 📊 Seções Disponíveis

### 1. **Autenticação e Segurança** (auth_system)

#### Perfis dos Utilizadores
- Gerir papéis dos utilizadores (Administrador, Médico, Atendente)
- Ver tentativas de login falhadas
- Bloquear/desbloquear contas
- Visualizar último acesso

#### Tentativas de Login
- Histórico completo de login
- IP Address de cada tentativa
- Status de sucesso/falha
- Timestamp de cada tentativa

#### Logs de Atividade
- Todas as ações no sistema (CREATE, UPDATE, DELETE)
- Utilizador responsável pela ação
- IP Address e User-Agent
- Data e hora exata

#### Utilizadores (Django Auth)
- Criar novos utilizadores
- Editar dados pessoais
- Atribuir permissões
- Ver histórico de acesso

---

### 2. **Clientes** (Pacientes)

#### Pacientes
- Registar novos pacientes
- Editar dados de pacientes
- Visualizar histórico de consultas
- Gerir estado (Ativo/Inativo/Suspenso)

#### Contratos
- Gerir contratos com pacientes
- Definir tarifas
- Visualizar períodos de contrato

---

### 3. **Equipamentos** (Recursos Médicos)

#### Contadores/Recursos
- Registar novos recursos médicos
- Gerir disponibilidade
- Atribuir a departamentos

---

### 4. **Pagamentos** (Consultas)

#### Faturas (Consultas)
- Registar consultas
- Gerir status (Pendente/Pago/Cancelado)
- Visualizar histórico

#### Recargas (Agendamentos)
- Agendar consultas
- Confirmar pagamentos
- Controlar disponibilidade

#### Recibos (Relatórios)
- Emitir recibos
- Registar pagamentos

---

## 🔐 Funções por Perfil

### 👨‍💼 **Administrador**
- ✅ Acesso total ao sistema
- ✅ Gerir utilizadores
- ✅ Ver logs de atividade
- ✅ Configurar sistema
- ✅ Exportar relatórios

### 👨‍⚕️ **Médico**
- ✅ Ver pacientes
- ✅ Registar consultas
- ✅ Visualizar histórico de pacientes
- ❌ Não pode gerir utilizadores

### 👨‍💻 **Atendente**
- ✅ Registar pacientes
- ✅ Agendar consultas
- ✅ Gerar recibos
- ❌ Não pode editar dados sensíveis

---

## 🛡️ Segurança no Admin

### Proteções Implementadas:
- ✅ Login obrigatório
- ✅ Validação de permissões
- ✅ Auditoria de todas as ações
- ✅ Rate limiting após 5 tentativas falhadas
- ✅ Bloqueio de conta por 15 minutos

### Boas Práticas:
1. **Mude a senha padrão** imediatamente
2. **Crie utilizadores únicos** para cada pessoa
3. **Revise logs regularmente** para atividades suspeitas
4. **Faça backup dos dados** regularmente
5. **Nunca compartilhe credenciais** de admin

---

## 📝 Exemplos de Uso

### Criar novo Utilizador

1. Ir para **Autenticação e Autorização** → **Utilizadores**
2. Clicar em **Adicionar Utilizador**
3. Preencher:
   - Utilizador
   - Senha (mínimo 6 caracteres)
   - Email
   - Nome Completo
4. Salvar
5. Ir para **auth_system** → **Perfis dos Utilizadores**
6. Criar perfil com o papel apropriado

### Registar novo Paciente

1. Ir para **Clientes** → **Pacientes**
2. Clicar em **Adicionar Paciente**
3. Preencher dados:
   - Nome completo
   - NIF/BI
   - Morada
   - Telefone
   - Email (opcional)
4. Selecionar tipo (Pré-pago/Pós-pago)
5. Salvar

### Ver Logs de Atividade

1. Ir para **auth_system** → **Logs de Atividade**
2. Filtrar por:
   - Utilizador
   - Ação (CREATE, UPDATE, DELETE)
   - Data
3. Buscar por IP ou recurso

---

## 🆘 Troubleshooting

### "Acesso Negado" ao Admin
- Verificar se o utilizador tem permissão (is_staff ou is_superuser)
- Verificar se a conta está ativa
- Fazer login novamente

### "Formulário inválido" ao criar
- Verificar campos obrigatórios
- Validar formatos (email, telefone)
- Tentar novamente com dados válidos

### Não consigo ver um módulo
- Verificar permissões do utilizador
- Tentar fazer logout e login novamente
- Contactar administrador

---

## 📞 Suporte

Para questões sobre o painel administrativo:
1. Contactar o administrador do sistema
2. Consultar logs de atividade para diagnosticar
3. Verificar permissões do utilizador

**Versão:** 1.0  
**Data:** Dezembro 2025  
**Hospital:** Malanje

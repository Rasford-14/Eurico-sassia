turma=[]
while True:
 nome=input("Inserir o nome do nome : ")

 nota= int(input("digita a nota do aluno:  "))
 matricula= int(input("Digite o nº estudante:  "))

# Verifica aprovação
 if nota >= 10:
        resultado = "Aprovado ✅"
 else:
        resultado = "Reprovado ❌"
    
 print(f"→ {nome}: {resultado}")
    


 alunos = {
        "nome": nome,
        "nota": nota,
        "matricula": matricula,
        "resultado": resultado
    }


 turma.append(alunos)
 RESP =input("QUERterminar[S/N]")


 if RESP  == "S" :
  break
# Cálculos finais
print("\n" + "="*2)
print("📋 RESULTADOS DA TURMA")
print("="*2)

# Soma das notas e média
soma_notas = sum(aluno["nota"] for aluno in turma)
media_turma = soma_notas / len(turma)

# Maior nota
maior_nota = max(aluno["nota"] for aluno in turma)
alunos_maior_nota = [a["nome"] for a in turma if a["nota"] == maior_nota]

# Menor nota
menor_nota = min(aluno["nota"] for aluno in turma)

# Aprovados e reprovados
aprovados = [a["nome"] for a in turma if a["nota"] >= 10]
reprovados = [a["nome"] for a in turma if a["nota"] < 10]

# 📝 Exibição dos resultados
print(f"📈 Número total de alunos: {len(turma)}")
print(f"📊 Média das notas da turma: {media_turma:.1f} valores")
print(f"🏆 Maior nota: {maior_nota} — Aluno(s): {', '.join(alunos_maior_nota)}")
print(f"📉 Menor nota: {menor_nota}")
print(f"✅ Aprovados ({len(aprovados)}): {', '.join(aprovados) if aprovados else 'Nenhum'}")
print(f"❌ Reprovados ({len(reprovados)}): {', '.join(reprovados) if reprovados else 'Nenhum'}")
print("="*40)
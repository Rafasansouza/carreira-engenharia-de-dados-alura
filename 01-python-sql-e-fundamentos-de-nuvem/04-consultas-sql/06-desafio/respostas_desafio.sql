-- 1. Buscar o nome do professor e a turma que ele é orientador
SELECT 	nome_professor, nome_turma 
FROM Professores P 
JOIN Turmas T ON P.ID_Professor = T.ID_Professor_Orientador;

-- 2. Retornar o nome e a nota do aluno que possui a melhor nota na disciplina de Matemática
SELECT nome_aluno, MAX(nota)  as maior_nota
FROM Alunos A
JOIN Notas N ON A.ID_Aluno = N.ID_Aluno
JOIN Disciplinas D ON D.ID_Disciplina = N.ID_Disciplina 
WHERE N.ID_Disciplina = 1;

-- 3. Identificar o total de alunos por turma
SELECT nome_turma, COUNT(TA.ID_Turma) Total_alunos_turma
FROM Turmas T
JOIN Turma_Alunos TA
ON T.ID_Turma = TA.ID_Turma
GROUP BY nome_turma;

--4. Listar os Alunos e as disciplinas em que estão matriculados
SELECT A.Nome_Aluno, D.Nome_Disciplina
from Alunos A 
join Turma_Alunos TA on A.ID_Aluno = TA.ID_Aluno
join Turma_Disciplinas TD on TA.ID_Turma = TD.ID_Turma
join Disciplinas D ON D.ID_Disciplina = TD.ID_Disciplina;

--5. Criar uma view que apresenta o nome, a disciplina e a nota dos alunos
CREATE VIEW AlunosDisciplinaNota AS
SELECT nome_aluno, nome_disciplina, nota 
FROM Alunos A
JOIN Notas N
ON A.ID_Aluno = N.ID_Aluno
Join Disciplinas D
On N.ID_Disciplina = D.ID_Disciplina;
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9a5db8c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['VEJA EXEMPLOS DE MODELOS DE CURRÍCULO', 'MODELO 1 – INDICADO PARA ESTÁGIO, PRIMEIRO EMPREGO, APRENDIZ.', 'Nome do candidato', 'Nacionalidade, estado civil e idade', 'Endereço – Bairro – Região (se necessário) - Cidade', 'Telefone residencial e celular', 'E-mail', 'Objetivo', 'No início da vida profissional não é necessário ter um objetivo totalmente definido. Os candidatos podem apenas citar a área de interesse.', 'Exemplo: Área financeira', 'Formação Acadêmica', 'Curso: Ciências Atuariais', 'Faculdade: (Nome da universidade)', 'Turno: ', 'Previsão de graduação: Jan/2010 – Dez/2015', '', 'Idiomas', 'Inglês Avançado', 'Espanhol Intermediário', '', 'Experiência Profissional ', 'Candidatos também podem colocar trabalho eventual ou em empresa júnior, do centro acadêmico da faculdade.', '', 'Nome da empresa', 'Cargo: Estagiário', 'Período: Fevereiro/2013 – Atual', '', 'Atribuições: Programar e controlar as reservas financeiras dos clientes, a fim de garantir o pagamento dos compromissos assumidos com os segurados; elaboração de planilhas e cálculos financeiros.', 'Outras atividades', 'Se o candidato faz trabalhos voluntários é importante descrever. O recrutador pode avaliar as habilidades através deles.', '', 'Exemplo: Trabalho voluntário na Paróquia Santo Antônio desde março de 2009.', 'Arrecadação de fundos para a paróquia, aulas de catequese, campanhas beneficentes para a comunidade.', '', '', '', '', '', 'MODELO 2 – INDICADO PARA CARGOS OPERACIONAIS', '', 'Nome do candidato', 'Nacionalidade, estado civil e idade', 'Endereço – Bairro – Região (se necessário) – Cidade', 'Telefone residencial – Celular:', 'E-mail', 'Objetivo Profissional', 'Recepcionista Atendente', '', 'Experiência Profissional', 'Nome da empresa', 'Cargo: Recepcionista Atendente', 'Período: De 08/2005 a 02/2013', 'Atribuições: Descreva suas atividades e responsabilidades na instituição Exemplo: Recepção e atendimento aos clientes; atendimento telefônico; elaboração de planilhas e relatórios; organização do local de trabalho; controle de a entrada e saída de visitantes; responsável pela guarda e controle das chaves; organização e distribuição de correspondências para os destinatários.', 'Formação Acadêmica', 'Ensino Médio Completo – Nome da instituição – Conclusão: ano de conclusão', '', 'Informática', 'Se não possuir conhecimentos em informática e/ou idiomas não mencione.', 'Exemplo: Pacote Office, Internet.', '', '', '', '', '', '', '', '', '', '']\n"
     ]
    }
   ],
   "source": [
    "from typing import List\n",
    "from dataclasses import dataclass, field\n",
    "from docx import Document\n",
    "from docx.opc.exceptions import PackageNotFoundError\n",
    "\n",
    "@dataclass\n",
    "class FormatFilter:\n",
    "    bold: List or str = field(default_factory = lambda: [\"None\", \"True\"])\n",
    "\n",
    "class ReadDocFile:\n",
    "    def __init__(self, filename):\n",
    "        self.fname = filename\n",
    "        self.loaded_document = None\n",
    "        self.content = None\n",
    "\n",
    "    def load_document(self):\n",
    "        try:\n",
    "            self.loaded_document = Document(self.fname)\n",
    "            self.content = self.get_content_as_list()\n",
    "        except PackageNotFoundError as e:\n",
    "            print(f\"File not found: {self.fname}\")\n",
    "            quit()\n",
    "\n",
    "    def get_content_as_list(self):\n",
    "        return [paragraph.text for paragraph in self.loaded_document.paragraphs]   \n",
    "\n",
    "if __name__ == \"__main__\" :\n",
    "    doc = ReadDocFile(\"cv.docx\")\n",
    "    doc.load_document()\n",
    "    print(doc.get_content_as_list())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8e73b64",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

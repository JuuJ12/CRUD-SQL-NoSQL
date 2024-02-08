-- Criar a tabela regioes
CREATE TABLE regioes (
  regiaoID CHAR(2) NOT NULL DEFAULT '',
  nomeRegiao VARCHAR(30) NOT NULL DEFAULT '',
  estadoRegiao VARCHAR(30) NOT NULL DEFAULT '',
  PRIMARY KEY (regiaoID)
);

-- Criar a tabela vinicolas
CREATE TABLE vinicolas (
  vinicolaID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nomeVinicola CHAR(2) NOT NULL DEFAULT '',
  foneVinicola INT UNSIGNED NOT NULL,
  regiaoID CHAR(2) NOT NULL DEFAULT '',
  PRIMARY KEY (vinicolaID),
  FOREIGN KEY (regiaoID) REFERENCES regioes (regiaoID)
);

-- Criar a tabela vinhos
CREATE TABLE vinhos (
  vinhoID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nomeVinho CHAR(2) NOT NULL DEFAULT '',
  tipoVinho VARCHAR(6) NOT NULL DEFAULT '',
  precoVinho DECIMAL(7,2) NOT NULL DEFAULT 99999.98,
  vinicolaID INT UNSIGNED NOT NULL,
  PRIMARY KEY (vinhoID),
  FOREIGN KEY (vinicolaID) REFERENCES vinicolas (vinicolaID)
);

-- Inserir dados na tabela regioes
INSERT INTO regioes VALUES
  ('R1', 'Vale S. Francico', 'Pernambuco'),
  ('R2', 'Zona da Mata', 'Pernambuco'),
  ('R3', 'Garibaldi', 'Rio Grande do Sul'),
  ('R4', 'Gramado', 'Rio Grande do Sul');
  
-- Inserir dados na tabela vinicolas
INSERT INTO vinicolas VALUES
  (1, 'A1', 1234, 'R1'),
  (2, 'A2', 5234, 'R1'),
  (3, 'A3', 6234, 'R2'),
  (4, 'A4', 7234, 'R2'),
  (5, 'A5', 8234, 'R3');

-- Inserir dados na tabela vinhos

INSERT INTO vinhos VALUES
  (10, 'V1', 'tinto', 100.00, 1),
  (20, 'V2', 'branco', 200.00, 1),
  (30, 'V3', 'rose', 300.00, 1),
  (40, 'V4', 'rose', 350.00, 2),
  (50, 'V5', 'branco', 250.00, 2),
  (60, 'V6', 'tinto', 150.00, 2),
  (70, 'V7', 'tinto', 397.00, 3),
  (80, 'V8', 'branco', 333.00, 3);

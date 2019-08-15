# Sample Visitor for PLSQL grammar

This repo contains  
├── generated  
│   ├── plsqlLexer.py  
│   ├── plsqlParser.py  
│   └── plsqlVisitor.py  
├── main.py  
├── sample_files  
│   └── create_tables_samples.sql  
└── source_grammar  
    └── plsql.g4  

main.py - File that contains code for modified Visitor  
source_grammar - Contains grammar for plsql (courtesy: https://github.com/datacamp/antlr-plsql)  
sample_files - Contains a sample file with plsql code (courtesy: https://github.com/antlr/grammars-v4)  
generated - Contains code generated using ANTLR4 from the forementioned grammar  
	Generated using: `antlr4 -visitor ./simple_source/plsql.g4 -no-listener -o generated/ -Dlanguage=Python3 -Xexact-output-dir`  

# Usage
Command: `python main.py ./sample_files/create_tables_samples.sql`

FROM python:3.9
COPY . .
RUN pip install mysql-connector-python pandas
CMD ["python ", "connectionUseTable.py" ,"CreateMySql_Table.py" ]

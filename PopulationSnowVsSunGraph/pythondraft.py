from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
#Starting the data magic. This takes five boxes
engine = create_engine("sqlite:///citypop.db")
engine
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
#Getting all the stuff set so it databass properly
Base.classes.keys()
onlytable=Base.classes.onlytable2
session = Session(engine)
inspector=inspect(engine)

#Putting the DB into a dataframe
dataframe = pd.read_sql_query("SELECT * FROM onlytable2", engine)

#Putting the dataframe into a Panda
dataframe_PD=pd.DataFrame.from_records(dataframe,columns=['date', 'SNOW', 'NOSNOW'])
dataframe_PD.set_index(["date"])

#Getting the variable types right
dataframe_PD['SNOW']=pd.to_numeric(dataframe_PD['SNOW'])
dataframe_PD['NOSNOW']=pd.to_numeric(dataframe_PD['NOSNOW'])

#PLOTLY!
lines=dataframe_PD.plot.line(x='date',y='SNOW')
lines=dataframe_PD.plot.line(x='date',y='NOSNOW')
plt.savefig('precipitationplot.png')
plt.show()
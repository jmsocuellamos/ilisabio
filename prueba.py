{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red245\green245\blue245;\red0\green0\blue0;
\red0\green0\blue255;\red157\green0\blue210;\red144\green1\blue18;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c0\c0\c100000;\cssrgb\c68627\c0\c85882;\cssrgb\c63922\c8235\c8235;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 ## Libreria scikit-survival\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 !\cf0 \strokec4 pip install scikit-survival\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 ## Librerias de tratamiento de datos y entorno gr\'e1fico\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 import\cf0 \strokec4  os\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  numpy \cf6 \strokec6 as\cf0 \strokec4  np      \cf2 \strokec2 # importamos numpy como np\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  pandas \cf6 \strokec6 as\cf0 \strokec4  pd     \cf2 \strokec2 # importamos pandas como pd\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  math             \cf2 \strokec2 # importamos m\'f3dulo para c\'e1culos matem\'e1ticos\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  random\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Configuraci\'f3n de entorno gr\'e1fico\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 ######################################\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 %matplotlib \cf0 \strokec4 inline\cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 import\cf0 \strokec4  matplotlib.pyplot \cf6 \strokec6 as\cf0 \strokec4  plt \cf2 \strokec2 # importamos matplotlib como plt\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  seaborn \cf6 \strokec6 as\cf0 \strokec4  sns \cf2 \strokec2 # importamos seaborn como sns\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 sns.set_style(\cf7 \strokec7 "ticks"\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 %config \cf0 \strokec4 InlineBackend.figure_format = \cf7 \strokec7 'retina'\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # M\'f3dulos scikit-survival\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 ###########################\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 from\cf0 \strokec4  sksurv.linear_model \cf6 \strokec6 import\cf0 \strokec4  CoxPHSurvivalAnalysis, CoxnetSurvivalAnalysis\cb1 \
\cf6 \cb3 \strokec6 from\cf0 \strokec4  sksurv.ensemble \cf6 \strokec6 import\cf0 \strokec4  RandomSurvivalForest\cb1 \
\cf6 \cb3 \strokec6 from\cf0 \strokec4  sksurv.metrics \cf6 \strokec6 import\cf0 \strokec4  (\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     concordance_index_censored,concordance_index_ipcw,cumulative_dynamic_auc\cb1 \
\cb3 )\cb1 \
}
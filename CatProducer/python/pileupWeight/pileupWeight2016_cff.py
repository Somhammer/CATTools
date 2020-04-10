import FWCore.ParameterSet.Config as cms

pileupWeightMap = {
#from SimGeneral/MixingModule/python/mix_2016_25ns_Moriond17MC_PoissonOOTPU_cfi.py
"2016_25ns_Moriond17MC":cms.vdouble(
1.78653e-05,2.56602e-05,5.27857e-05,8.88954e-05,0.000109362,
0.000140973,0.000240998,0.00071209 ,0.00130121 ,0.00245255 ,
0.00502589 ,0.00919534 ,0.0146697  ,0.0204126  ,0.0267586  ,
0.0337697  ,0.0401478  ,0.0450159  ,0.0490577  ,0.0524855  ,
0.0548159  ,0.0559937  ,0.0554468  ,0.0537687  ,0.0512055  ,
0.0476713  ,0.0435312  ,0.0393107  ,0.0349812  ,0.0307413  ,
0.0272425  ,0.0237115  ,0.0208329  ,0.0182459  ,0.0160712  ,
0.0142498  ,0.012804   ,0.011571   ,0.010547   ,0.00959489 ,
0.00891718 ,0.00829292 ,0.0076195  ,0.0069806  ,0.0062025  ,
0.00546581 ,0.00484127 ,0.00407168 ,0.00337681 ,0.00269893 ,
0.00212473 ,0.00160208 ,0.00117884 ,0.000859662,0.000569085,
0.000365431,0.000243565,0.00015688 ,9.88128e-05,6.53783e-05,
3.73924e-05,2.61382e-05,2.0307e-05 ,1.73032e-05,1.435e-05  ,
1.36486e-05,1.35555e-05,1.37491e-05,1.34255e-05,1.33987e-05,
1.34061e-05,1.34211e-05,1.34177e-05,1.32959e-05,1.33287e-05
),
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/PileupHistogram-goldenJSON-13tev-2016-69200ub-75bins.root
"Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON":cms.vdouble(
238797,837471.4,2297400,3120461,4467047,
5978968,6993394,1.287076e+07,3.521554e+07,7.863183e+07,
1.768482e+08,3.599176e+08,6.024208e+08,8.758292e+08,1.173179e+09,
1.486844e+09,1.755957e+09,1.939293e+09,2.043571e+09,2.095604e+09,
2.127177e+09,2.144481e+09,2.125659e+09,2.060554e+09,1.961732e+09,
1.841319e+09,1.703904e+09,1.554438e+09,1.399462e+09,1.243525e+09,
1.088819e+09,9.373043e+08,7.92044e+08,6.567177e+08,5.344668e+08,
4.271268e+08,3.351056e+08,2.577246e+08,1.937514e+08,1.418309e+08,
1.006714e+08,6.901386e+07,4.554008e+07,2.884748e+07,1.750632e+07,
1.016264e+07,5637781,2987282,1512002,731845.4,
339822,152545.4,67404.82,30489.69,15152.11,
8975.911,6496.155,5434.805,4889.958,4521.716,
4208.464,3909.763,3614.274,3320.722,3031.096,
2748.237,2474.977,2213.817,1966.815,1735.546,
1521.109,1324.149,1144.898,983.2202,838.6676
),
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/PileupHistogram-goldenJSON-13tev-2016-72400ub.root
"Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON_Up":cms.vdouble(
232655.3,658640.6,2174438,2737620,4063955,
5379260,6375381,9014024,2.369742e+07,5.384191e+07,
1.15685e+08,2.454186e+08,4.424094e+08,6.787255e+08,9.359048e+08,
1.216e+09,1.497929e+09,1.725772e+09,1.877085e+09,1.962515e+09,
2.006332e+09,2.034455e+09,2.049846e+09,2.033425e+09,1.976201e+09,
1.888393e+09,1.780949e+09,1.658122e+09,1.523601e+09,1.382864e+09,
1.240384e+09,1.098451e+09,9.585305e+08,8.227756e+08,6.941486e+08,
5.756199e+08,4.693739e+08,3.764348e+08,2.967622e+08,2.295858e+08,
1.738156e+08,1.283265e+08,9.205136e+07,6.393789e+07,4.287888e+07,
2.769986e+07,1.720651e+07,1.026401e+07,5874311,3223993,
1696756,856939,416220.6,195427.7,89753.45,
41366.99,20107.76,11085.64,7328.995,5735.958,
4991.836,4564.5,4248.039,3966.694,3694.715,
3424.962,3156.98,2892.56,2634.092,2383.944,
2144.221,1916.678,1702.686,1503.231,1318.937
),
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/PileupHistogram-goldenJSON-13tev-2016-66000ub.root
"Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON_Dn":cms.vdouble(
247463.1,1070388,2416060,3566468,4981296,
6581823,8095227,1.997782e+07,5.195852e+07,1.19964e+08,
2.732287e+08,5.137839e+08,8.028937e+08,1.119018e+09,1.46256e+09,
1.77845e+09,2.001764e+09,2.130222e+09,2.192957e+09,2.228725e+09,
2.24827e+09,2.226559e+09,2.152103e+09,2.04036e+09,1.904702e+09,
1.750313e+09,1.583824e+09,1.412782e+09,1.241647e+09,1.0727e+09,
9.088083e+08,7.541516e+08,6.129875e+08,4.883017e+08,3.812529e+08,
2.91425e+08,2.174756e+08,1.57775e+08,1.107438e+08,7.48592e+07,
4.853905e+07,3.009452e+07,1.779958e+07,1.002583e+07,5372007,
2736760,1325993,612045.7,270409.1,115717.5,
49339.23,22255.09,11661.83,7607.37,6005.958,
5274.752,4833.322,4480.216,4150.23,3825.111,
3502.165,3183.554,2872.682,2572.963,2287.392,
2018.393,1767.784,1536.78,1326.033,1135.686,
965.4373,814.6162,682.2534,567.1563,467.977
)
}
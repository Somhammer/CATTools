import FWCore.ParameterSet.Config as cms

pileupWeightMap = {
#from SimGeneral/MixingModule/python/mix_2017_25ns_WinterMC_PUScenarioV1_PoissonOOTPU_cfi.py
"2018_25ns_MC":cms.vdouble(
4.695341e-10, 1.206213e-06, 1.162593e-06, 6.118058e-06, 1.626767e-05,
3.508135e-05, 7.12608e-05, 0.0001400641, 0.0002663403, 0.0004867473,
0.0008469, 0.001394142, 0.002169081, 0.003198514, 0.004491138,
0.006036423, 0.007806509, 0.00976048, 0.0118498, 0.01402411,
0.01623639, 0.01844593, 0.02061956, 0.02273221, 0.02476554,
0.02670494, 0.02853662, 0.03024538, 0.03181323, 0.03321895,
0.03443884, 0.035448, 0.03622242, 0.03674106, 0.0369877,
0.03695224, 0.03663157, 0.03602986, 0.03515857, 0.03403612,
0.0326868, 0.03113936, 0.02942582, 0.02757999, 0.02563551,
0.02362497, 0.02158003, 0.01953143, 0.01750863, 0.01553934,
0.01364905, 0.01186035, 0.01019246, 0.008660705, 0.007275915,
0.006043917, 0.004965276, 0.004035611, 0.003246373, 0.002585932,
0.002040746, 0.001596402, 0.001238498, 0.0009533139, 0.0007282885,
0.000552306, 0.0004158005, 0.0003107302, 0.0002304612, 0.0001696012,
0.0001238161, 8.96531e-05, 6.438087e-05, 4.585302e-05, 3.23949e-05,
2.271048e-05, 1.580622e-05, 1.09286e-05, 7.512748e-06, 5.140304e-06,
3.505254e-06, 2.386437e-06, 1.625859e-06, 1.111865e-06, 7.663272e-07,
5.350694e-07, 3.808318e-07, 2.781785e-07, 2.098661e-07, 1.642811e-07,
1.312835e-07, 1.081326e-07, 9.141993e-08, 7.890983e-08, 6.91468e-08,
6.119019e-08, 5.443693e-08, 4.85036e-08, 4.31486e-08, 3.822112e-08
),
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt --inputLumiJSON /CATTools/CatProducer/data/LumiMask/pileup_latest.txt --minBiasXsec 69200 --calcMode true --maxPileupBin 100 --numPileupBins 100 PileUpData.root 
"Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON":cms.vdouble(
2.913074e+05,1.022577e+06,3.120230e+06,6.816540e+06,1.200576e+07,
1.863058e+07,2.746169e+07,3.995269e+07,5.648620e+07,7.824153e+07,
1.089914e+08,1.525342e+08,2.120739e+08,2.900471e+08,3.885491e+08,
5.096515e+08,6.544826e+08,8.217964e+08,1.006735e+09,1.200380e+09,
1.390683e+09,1.565093e+09,1.714186e+09,1.834537e+09,1.928951e+09,
2.004022e+09,2.067052e+09,2.123836e+09,2.177652e+09,2.229293e+09,
2.277572e+09,2.320055e+09,2.353737e+09,2.375400e+09,2.381655e+09,
2.368968e+09,2.333780e+09,2.272938e+09,2.184334e+09,2.067545e+09,
1.924284e+09,1.758493e+09,1.576058e+09,1.384201e+09,1.190665e+09,
1.002889e+09,8.272599e+08,6.685818e+08,5.298358e+08,4.121856e+08,
3.152271e+08,2.373817e+08,1.763379e+08,1.294575e+08,9.409591e+07,
6.782370e+07,4.854434e+07,3.453375e+07,2.442857e+07,1.718309e+07,
1.201356e+07,8.342427e+06,5.748666e+06,3.927151e+06,2.657267e+06,
1.779583e+06,1.178951e+06,7.723895e+05,5.003877e+05,3.205961e+05,
2.031936e+05,1.274455e+05,7.913752e+04,4.866967e+04,2.965497e+04,
1.790595e+04,1.071511e+04,6.354312e+03,3.733571e+03,2.172796e+03,
1.251877e+03,7.137229e+02,4.024207e+02,2.242658e+02,1.234607e+02,
6.710229e+01,3.598839e+01,1.903682e+01,9.927560e+00,5.101928e+00,
2.582949e+00,1.287805e+00,6.321441e-01,3.054270e-01,1.452214e-01,
6.793657e-02,3.126472e-02,1.415210e-02,6.300093e-03,2.757942e-03,
),
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt --inputLumiJSON /CATTools/CatProducer/data/LumiMask/pileup_latest.txt --minBiasXsec 72383 --calcMode true --maxPileupBin 100 --numPileupBins 100 PileUpData_Up.root 
"Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON_Up":cms.vdouble(
2.702466e+05,8.961790e+05,2.676487e+06,5.875395e+06,1.037143e+07, 
1.614760e+07,2.351601e+07,3.381228e+07,4.761990e+07,6.528072e+07,
8.926512e+07,1.229958e+08,1.693487e+08,2.307365e+08,3.089672e+08,
4.058200e+08,5.228938e+08,6.606889e+08,8.174967e+08,9.885545e+08,
1.165879e+09,1.339174e+09,1.498003e+09,1.634589e+09,1.746003e+09,
1.834372e+09,1.905048e+09,1.964213e+09,2.017051e+09,2.066814e+09,
2.114695e+09,2.160166e+09,2.201482e+09,2.236275e+09,2.261911e+09,
2.275637e+09,2.274557e+09,2.255688e+09,2.216115e+09,2.153427e+09,
2.066201e+09,1.954487e+09,1.820085e+09,1.666566e+09,1.499004e+09,
1.323493e+09,1.146511e+09,9.742962e+08,8.122654e+08,6.645962e+08,
5.340186e+08,4.217942e+08,3.278708e+08,2.511685e+08,1.899133e+08,
1.419637e+08,1.050821e+08,7.713671e+07,5.622670e+07,4.073940e+07,
2.936011e+07,2.105149e+07,1.501535e+07,1.064926e+07,7.504738e+06,
5.250854e+06,3.644497e+06,2.507397e+06,1.708869e+06,1.153172e+06,
7.703024e+05,5.093016e+05,3.333288e+05,2.159984e+05,1.386259e+05,
8.814761e+04,5.555281e+04,3.471110e+04,2.150803e+04,1.321781e+04,
8.056541e+03,4.869877e+03,2.918549e+03,1.733610e+03,1.020219e+03,
5.945541e+02,3.429498e+02,1.957002e+02,1.104223e+02,6.157703e+01,
3.392190e+01,1.845265e+01,9.908043e+00,5.249478e+00,2.743516e+00,
1.413971e+00,7.184674e-01,3.598418e-01,1.776108e-01,8.637860e-02,
),
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt --inputLumiJSON /CATTools/CatProducer/data/LumiMask/pileup_latest.txt --minBiasXsec 66016 --calcMode true --maxPileupBin 100 --numPileupBins 100 PileUpData_Dn.root 
"Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON_Dn":cms.vdouble(
3.158084e+05,1.178589e+06,3.661347e+06,7.955396e+06,1.398014e+07,
2.169199e+07,3.245225e+07,4.767597e+07,6.773850e+07,9.539745e+07,
1.355271e+08,1.923283e+08,2.692128e+08,3.687733e+08,4.935735e+08,
6.454957e+08,8.239737e+08,1.024217e+09,1.236326e+09,1.446165e+09,
1.638541e+09,1.801935e+09,1.932317e+09,2.033405e+09,2.113364e+09,
2.180819e+09,2.242181e+09,2.300613e+09,2.356283e+09,2.407134e+09,
2.449892e+09,2.480785e+09,2.495830e+09,2.490833e+09,2.461479e+09,
2.403713e+09,2.314524e+09,2.192807e+09,2.040053e+09,1.860580e+09,
1.661234e+09,1.450635e+09,1.238112e+09,1.032608e+09,8.417012e+08,
6.709282e+08,5.235066e+08,4.003989e+08,3.006968e+08,2.221670e+08,
1.618312e+08,1.164663e+08,8.297684e+07,5.862434e+07,4.112658e+07,
2.866917e+07,1.986258e+07,1.367206e+07,9.342876e+06,6.331882e+06,
4.251186e+06,2.824617e+06,1.855690e+06,1.204705e+06,7.725699e+05,
4.893809e+05,3.062520e+05,1.894005e+05,1.158103e+05,7.004651e+04,
4.192670e+04,2.484325e+04,1.457554e+04,8.467375e+03,4.869819e+03,
2.771892e+03,1.560770e+03,8.688702e+02,4.779149e+02,2.595605e+02,
1.391013e+02,7.351058e+01,3.828533e+01,1.963978e+01,9.918427e+00,
4.928936e+00,2.409309e+00,1.157992e+00,5.470874e-01,2.539960e-01,
1.158543e-01,5.190659e-02,2.283911e-02,9.867650e-03,4.185688e-03,
1.742957e-03,7.124061e-04,2.857918e-04,1.125179e-04,4.347161e-05,
),
}
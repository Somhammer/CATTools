import FWCore.ParameterSet.Config as cms
import os
process = cms.Process("h2muAnalyzer")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(True)

process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/v7-4-5_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/151109_232735/0000/catTuple_88.root')
    #fileNames = cms.untracked.vstring('root://cms-xrdr.sdfarm.kr:1094//xrd/store/group/CAT/DoubleMuon/v7-4-4_Run2015C_25ns-05Oct2015-v1/151023_165157/0000/catTuple_10.root')
    fileNames = cms.untracked.vstring('file:%s/src/CATTools/CatProducer/prod/catTuple.root'%os.environ["CMSSW_BASE"])
)

useGold = True
isRunData = False
catmet = 'catMETsNoHF'
if useGold:
    catmet = 'catMETs'
    if isRunData:
        lumiFile = 'Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
        from FWCore.PythonUtilities.LumiList import LumiList
        lumiList = LumiList(os.environ["CMSSW_BASE"]+'/src/CATTools/CatProducer/prod/LumiMask/'+lumiFile)
        process.source.lumisToProcess = lumiList.getVLuminosityBlockRange()
    
    process.load("CATTools.CatProducer.pileupWeight_cff")                # loads pileup weighting tool
    from CATTools.CatProducer.pileupWeight_cff import pileupWeightMap
    process.pileupWeight.weightingMethod = "RedoWeight"                  # set mode to reweighting
    process.pileupWeight.pileupMC = pileupWeightMap["Startup2015_25ns"]  # MC pileup distrubition 
    from pileup import pileupMap                                         # new pileup file made with getPileUpData.py
    process.pileupWeight.pileupRD = pileupMap["Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON"] # new data PU distrubition
    process.pileupWeight.pileupUp = pileupMap["Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Up"]
    process.pileupWeight.pileupDn = pileupMap["Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Dn"]

process.filterRECO = cms.EDFilter("CATTriggerBitCombiner",
    triggerResults = cms.InputTag("TriggerResults::PAT"),
    secondaryTriggerResults = cms.InputTag("TriggerResults::RECO"),
    triggerPrescales = cms.InputTag("patTrigger"),
    combineBy = cms.string("and"),
    triggersToMatch = cms.vstring(
        "CSCTightHaloFilter",
        #"EcalDeadCellTriggerPrimitiveFilter",
        #"HBHENoiseFilter",
        "eeBadScFilter",
        "goodVertices",
    ),
    doFilter = cms.bool(False),
)

process.cattree = cms.EDAnalyzer("h2muAnalyzer",
    recoFilters = cms.InputTag("filterRECO"),
    nGoodVertex = cms.InputTag("catVertex","nGoodPV"),
    genweight = cms.InputTag("genWeight","genWeight"),
    puweight = cms.InputTag("pileupWeight"),
    vertices = cms.InputTag("catVertex"),
    muons = cms.InputTag("catMuons"),
    electrons = cms.InputTag("catElectrons"),
    jets = cms.InputTag("catJets"),
    mets = cms.InputTag(catmet),
    mcLabel = cms.InputTag("prunedGenParticles"),
    triggerBits = cms.InputTag("TriggerResults","","HLT"),
    triggerObjects = cms.InputTag("catTrigger"),
    #triggerObjects = cms.InputTag("selectedPatTrigger"),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("cattree.root")
)

process.p = cms.Path(process.cattree)
#process.MessageLogger.cerr.FwkReport.reportEvery = 50000

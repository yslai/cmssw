# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run1_data -s RAW2DIGI,L1Reco,RECO,ALCA:SiStripCalZeroBias+SiStripCalMinBias+TkAlMinBiasHI+HcalCalMinBias,DQM --process reRECO -n 30 --data --eventcontent RECO,DQM --scenario HeavyIons --datatier RECO,DQMIO --repacked --filein filelist:step1_dasquery.log --lumiToProcess step1_lumiRanges.log --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('VS')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( (
"/store/relval/CMSSW_7_4_0_pre5/HIMinBiasUPC/RECO/GR_R_73_V0A_RelVal_hi2011-v1/00000/E8590D62-AC9D-E411-A7D9-02163E00E84A.root"
) ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:30'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.RECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_HIon', '')

process.GlobalTag.toGet = cms.VPSet( 
    cms.PSet(record = cms.string('HeavyIonUERcd'),
             tag = cms.string('UETable_PF_v00_mc'),
             connect = cms.untracked.string('sqlite_file:output.db'),
             label = cms.untracked.string('PF')
             )
)

#process.GlobalTag.toGet.extend([
#    cms.PSet(record = cms.string('HeavyIonRcd'),
#             tag = cms.string('UETable_PF_v_mc'),
#             connect = cms.untracked.string('sqlite_file:output.db'),
#             label = cms.untracked.string('PF')
#             )
#    ])



# Path and EndPath definitions
process.reconstruction_step = cms.Path(process.voronoiBackgroundPF)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)






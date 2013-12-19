#coding: utf8
import xlwt
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

#Create a style for font and its size for first line
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Arial'
#font.bold = True
font.height = 220
# Set the style's font to this new one you set up
style.font = font

#Create a style for font and its size for second line
style2 = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Arial'
#font.bold = True
font.height = 200
# Set the style's font to this new one you set up
style2.font = font

#split lines
string1 = 'callType, startTime, teleServiceCode, bearerServiceCode, volumeVolume, volumeUmcode, spNumberAddress, spNumberNumberingPlan, spNumberTypeOfNumber, spNumberClir, spNumberNetwork, spPort, spEquipmentNumber, spEquipmentClassMark, spLocation, netElementAddress, netElementNetwork, opNumberAddress, opNumberTypeOfNumber, opNumberNumberingPlan,Rating Group, routingNumberAddress, causeForForward, cugInfoCugInterLockCode, cugInfoCugInformation, cugInfoCugType, techInfoTermind, techInfoType, inTrunk, outTrunk, recordIdentificationCDRid, dataVolumeVolume, dataVolumeUmcode, messagesVolume, messagesUmcode, callTypeInfoXfileInd, sPNumberingPlan, spLocationNumberingPlan, routingNumberNumberingPlan, netElementNumberingPlan, upLinkVolumeVolume, downLinkVolumeVolume, upLinkVolumeUmcode, downLinkVolumeUmcode, startTimeDummy, servedPDPAddressAddress, servedPDPAddressNumberingplan, recordIdentificationOrigCdrId, qualityOfServiceNegotiatedDelay, qualityOfServiceNegotiatedPeakThroughput, qualityOfserviceNegotiatedMeanThroughput, qualityOfserviceNegotiatedPrecedence, qualityOfserviceNegotiatedReliability, sgsnAddressSgsnAddress, netElementEntity, netElementAddressNew, netElementNumberingPlanNew, callTypeInfoNetworkInitContextId, technicalInfoAnonymousAccess,Duration,CellID ,TimeZone,rATType,GGSN-Address,GPRS End Time,CauseForRecClosing,NodeId,SubscriberTypeÿ,ContentType,ServiceName,3gpp-Qos-Profile,Effective Duration,PDP-Type,Selection-Mode,TimeOfFirstUsage,TimeOfLastUsage,DataPacketDownlink,DataPacketUplink,LocalSequence,DataVolDownlinkTTC,GGSN-MCC-MNC,AcctSessionID,Roaming'
list1 = string1.decode('utf-8').split(',')
print list1
for i in range(1, 73):
	sheet.write(0,i-1,i, style)
for i in range(1, 73):
	sheet.write(1,i-1,list1[i-1], style)
wbk.save('text11.xls')
import os, commands, json
import json
from time import sleep

data = []

def load_data():
    with open(r"/home/thesis/Downloads/data_1.json", 'r') as file:
        data_1 = file.read()
    with open(r"/home/thesis/Downloads/data_2.json", 'r') as file:
        data_2 = file.read()
    with open(r"/home/thesis/Downloads/data_3.json", 'r') as file:
        data_3 = file.read()
    with open(r"/home/thesis/Downloads/data_4.json", 'r') as file:
        data_4 = file.read()
    
    data.append(json.dumps(data_1))
    data.append(json.dumps(data_2))
    data.append(json.dumps(data_3))
    data.append(json.dumps(data_4))
    return(data)

def getOrganInfoJson(organID):
    res = commands.getstatusoutput("docker exec -it cli peer chaincode invoke -o orderer.organ.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/organ.com/orderers/orderer.organ.com/msp/tlscacerts/tlsca.organ.com-cert.pem -C organ-channel -n organcc  --peerAddresses peer1.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer1.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer0.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer0.hospital.organ.com/tls/ca.crt   --peerAddresses peer1.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer1.hospital.organ.com/tls/ca.crt   --peerAddresses peer0.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer0.gp.organ.com/tls/ca.crt   --peerAddresses peer1.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer1.gp.organ.com/tls/ca.crt   --peerAddresses peer0.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer0.opo.organ.com/tls/ca.crt   --peerAddresses peer1.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer1.opo.organ.com/tls/ca.crt  -c '{\"Args\":[\"readOrgan\",\""+ str(organID) +"\"]}'")
    try:
        organ_json = json.loads(res[1].split('payload:')[1])
        organ_json = (json.loads(organ_json))
        organ_info_json = json.loads(organ_json["donorInfo"])
    except Exception as e:
        print e
        organ_info_json=""
    return organ_info_json

def getCandidateInfoJson(candidateID):
    try:
        res = commands.getstatusoutput("docker exec -it cli peer chaincode invoke -o orderer.organ.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/organ.com/orderers/orderer.organ.com/msp/tlscacerts/tlsca.organ.com-cert.pem -C organ-channel -n organcc  --peerAddresses peer1.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer1.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer0.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer0.hospital.organ.com/tls/ca.crt   --peerAddresses peer1.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer1.hospital.organ.com/tls/ca.crt   --peerAddresses peer0.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer0.gp.organ.com/tls/ca.crt   --peerAddresses peer1.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer1.gp.organ.com/tls/ca.crt   --peerAddresses peer0.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer0.opo.organ.com/tls/ca.crt   --peerAddresses peer1.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer1.opo.organ.com/tls/ca.crt  -c '{\"Args\":[\"readCandidate\",\""+ str(candidateID) +"\"]}'")
        organ_json = json.loads(res[1].split('payload:')[1])
        organ_json = (json.loads(organ_json))
        organ_info_json = json.loads(organ_json["candidateInfo"])
    except Exception as e:
        print e
        organ_info_json=''
    return organ_info_json

def addOrgan(organ_id = '', organ_name='', organ_data=''):
    cmd = "docker exec -it cli peer chaincode invoke -o orderer.organ.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/organ.com/orderers/orderer.organ.com/msp/tlscacerts/tlsca.organ.com-cert.pem -C organ-channel -n organcc  --peerAddresses peer1.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer1.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer0.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer0.hospital.organ.com/tls/ca.crt   --peerAddresses peer1.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer1.hospital.organ.com/tls/ca.crt   --peerAddresses peer0.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer0.gp.organ.com/tls/ca.crt   --peerAddresses peer1.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer1.gp.organ.com/tls/ca.crt   --peerAddresses peer0.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer0.opo.organ.com/tls/ca.crt   --peerAddresses peer1.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer1.opo.organ.com/tls/ca.crt  "
    cmd += ' -c \'{"Args":["initOrgan", "' + str(organ_id) + '", "' + str(organ_name) + '", ' + str(organ_data) + ']}\''
    # print(cmd)
    res = commands.getstatusoutput(cmd)
    organInfoJson = getOrganInfoJson(organ_id)
    # Get organInfo
    # Get all unmatched Candidates
    availableCandidates = getAllCandidates()
    # for each Candidate 
    print("Available Candidates %s" % availableCandidates)
    for candidate in availableCandidates:
    #      read candidate
        print("Checking Candidate %s" % candidate)
        candidateInfo = getCandidateInfoJson(candidate)
    #       Find match
        match = len(candidateInfo.keys())

        for key in candidateInfo.keys():
            if(candidateInfo[key]==organInfoJson[key]):
                match -=1
                continue
            else:
                break
        print("Match %s " % match )
        if(match <= 0):
            transfer(candidate, organ_id)
            print("%s candidate was matched with %s" % (candidate, organ_id))
        else:
            print("No available matching Candiate")
            break
    #       If matched then transfer
    # if match
    print(res)

def addCandidate(candidate_id = '', organ_name='', info=''):
    cmd = "docker exec -it cli peer chaincode invoke -o orderer.organ.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/organ.com/orderers/orderer.organ.com/msp/tlscacerts/tlsca.organ.com-cert.pem -C organ-channel -n organcc  --peerAddresses peer1.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer1.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer0.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer0.hospital.organ.com/tls/ca.crt   --peerAddresses peer1.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer1.hospital.organ.com/tls/ca.crt   --peerAddresses peer0.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer0.gp.organ.com/tls/ca.crt   --peerAddresses peer1.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer1.gp.organ.com/tls/ca.crt   --peerAddresses peer0.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer0.opo.organ.com/tls/ca.crt   --peerAddresses peer1.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer1.opo.organ.com/tls/ca.crt  "
    cmd += ' -c \'{"Args":["initCandidate", "' + candidate_id + '", "' + organ_name + '", ' + info + ']}\''
    res = commands.getstatusoutput(cmd)
    candidateInfoJson = getCandidateInfoJson(candidate_id)

    availableOrgans = getAllOrgans()

    for organ in availableOrgans:
        organInfo = getOrganInfoJson(organ)
        match = len(organInfo.keys())
        for key in organInfo.keys():
            if(organInfo[key] == candidateInfoJson[key]):
                match -= 1
                continue
            else:
                break
            if(match <= 0):
                transfer(candidate_id, organ)
                print("%s organ was alloted to %s" % (organ, candidate_id))
            else:
                print("No available Organ")
                break
    print(res)

def getAllOrgans():
    ''' Returns unmatched organs'''
    try:
        cmd = "docker exec -it cli peer chaincode invoke -o orderer.organ.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/organ.com/orderers/orderer.organ.com/msp/tlscacerts/tlsca.organ.com-cert.pem -C organ-channel -n organcc  --peerAddresses peer1.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer1.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer0.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer0.hospital.organ.com/tls/ca.crt   --peerAddresses peer1.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer1.hospital.organ.com/tls/ca.crt   --peerAddresses peer0.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer0.gp.organ.com/tls/ca.crt   --peerAddresses peer1.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer1.gp.organ.com/tls/ca.crt   --peerAddresses peer0.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer0.opo.organ.com/tls/ca.crt   --peerAddresses peer1.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer1.opo.organ.com/tls/ca.crt  "
        cmd +=  '-c \'{\"Args\":[\"queryAllorgans\"]}\''
        res = commands.getstatusoutput(cmd)
        res = res[1].strip(" \r')")
        res = res.split("payload:\"[")[1]
        res = res.strip("]\"")
        res = res.split(',')
        res = [int(val.split("\"")[1].strip('\\')) for val in res]
        
    except Exception as e:
        res = []
    print(res)
    return(res)

def getAllCandidates():
    ''' Returns unmatched Candidates'''
    try:
        cmd = "docker exec -it cli peer chaincode invoke -o orderer.organ.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/organ.com/orderers/orderer.organ.com/msp/tlscacerts/tlsca.organ.com-cert.pem -C organ-channel -n organcc  --peerAddresses peer1.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer1.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer0.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer0.hospital.organ.com/tls/ca.crt   --peerAddresses peer1.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer1.hospital.organ.com/tls/ca.crt   --peerAddresses peer0.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer0.gp.organ.com/tls/ca.crt   --peerAddresses peer1.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer1.gp.organ.com/tls/ca.crt   --peerAddresses peer0.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer0.opo.organ.com/tls/ca.crt   --peerAddresses peer1.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer1.opo.organ.com/tls/ca.crt  "
        cmd +=  '-c \'{\"Args\":[\"queryAllcandidates\"]}\''
        res = commands.getstatusoutput(cmd)
        res = res[1].strip(" \r')")
        res = res.split("payload:\"[")[1]
        res = res.strip("]\"")
        res = res.split(',')
        res = [int(val.split("\"")[1].strip('\\')) for val in res]
    except Exception as e:
        res = []
    print(res)
    return(res)

def findMatching():
    pass

def transfer(organid, candidateid):
    cmd = "docker exec -it cli peer chaincode invoke -o orderer.organ.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/organ.com/orderers/orderer.organ.com/msp/tlscacerts/tlsca.organ.com-cert.pem -C organ-channel -n organcc  --peerAddresses peer1.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer1.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.histocompatibility.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/histocompatibility.organ.com/peers/peer0.histocompatibility.organ.com/tls/ca.crt  --peerAddresses peer0.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer0.hospital.organ.com/tls/ca.crt   --peerAddresses peer1.hospital.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/hospital.organ.com/peers/peer1.hospital.organ.com/tls/ca.crt   --peerAddresses peer0.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer0.gp.organ.com/tls/ca.crt   --peerAddresses peer1.gp.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/gp.organ.com/peers/peer1.gp.organ.com/tls/ca.crt   --peerAddresses peer0.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer0.opo.organ.com/tls/ca.crt   --peerAddresses peer1.opo.organ.com:7051  --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/opo.organ.com/peers/peer1.opo.organ.com/tls/ca.crt  "
    cmd +=  '-c \'{\"Args\":[\"transferOrgan",\"' + str(organid) + '\",\"' + str(candidateid) + '\"]}\''
    commands.getstatusoutput(cmd)

def generateLoad():
    for i in range(15):
        cmd = addCandidate(str(i+8000), "Intestine", data[i%4])
        sleep(10)
        
    for i in range(15):
        cmd = addOrgan(str(i+4000), "Intestine", data[i%4])
        sleep(10)
        
    for i in range(15):
        cmd = getCandidateInfoJson(str(i+8000))
        print("getCandidateInfoJson %s" % (i+8000))
        sleep(10)
        
    for i in range(15):
        cmd = getOrganInfoJson(str(i+4000))
        print("getOrganInfoJson %s" % (i+4000))
        sleep(10)

if __name__ == "__main__":
    # getAllOrgans()
    # getAllCandidates()
    # print(type(getCandidateInfoJson("9010")))
    data = load_data()
    print("Data Loaded")
    # Test add organ
    print("Starting to generate Load.")
    generateLoad()
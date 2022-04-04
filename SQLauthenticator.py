import CoinObj
import mysql.connector
import time


class DatabaseLogin:

    def __init__(self):
        self.host = "null"
        self.user = "null"
        self.password = "null"
        self.database = "null"

    def setHost(self, host):
        self.host = host

    def __setUsername(self, user):
        self.user = user

    def __setPassword(self, password):
        self.password = password

    def setDatabase(self, database):
        self.database = database


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BishopRoss",
    database="test"
)

mycursor = mydb.cursor()

# mycursor = mycursor.execute("CREATE DATABASE test") mycursor.execute("CREATE TABLE ETHEREUM (COIN_ID VARCHAR (30),
# TOTAL_VOLUME DOUBLE PRECISION, PRICE DOUBLE PRECISION, BUY_VOLUME DOUBLE PRECISION, SELL_VOLUME DOUBLE PRECISION,
# MARKET_CAP DOUBLE PRECISION)")
# mycursor.execute("CREATE TABLE ethereum2 (PRICE float, TOTAL_VOLUME float, 30_DAY_VOLUME float)")

# mycursor.execute("CREATE TABLE ethereum3 (PRICE float, TOTAL_VOLUME float, 30_DAY_VOLUME float, "
# "OPENING_PRICE float, 24_HOUR_HIGH float,24_HOUR_LOW float, TIME datetime )")
# mycursor.execute("SHOW TABLES")


coins = ["0x", "1inch", "Aave", "Aergo", "Aioz_Network", "Alchemix", "Alchemy_Pay", "Adventure_Gold", "Algorand", "AMP",
         "Ampleforth_Governance_Token", "Ankr", "API3", "ARPA_Chain", "Assemble_Protocol", "Augur", "Avalanche",
         "Aventus", "Axie_Infinity", "Badger_DAO", "Balancer", "Bancor_Network_Token", "Band_Protocol", "BarnBridge",
         "Basic_Attention_Token", "Biconomy", "Bitcoin", "Bitcoin_Cash", "Bluzelle", "Bonfida", "Bounce_Token_AUC",
         "Braintrust", "Cardano", "Cartesi", "Celo", "Chainlink", "Chiliz", "Civic", "Clover_Finance", "Compound",
         "Cosmos", "COTI", "COVAL", "Cryptex_Finance", "Crypto_com_Chain", "Curve_DAO_Token", "Dai", "Dash",
         "Decentraland", "Decentralized_Social", "DerivaDAO", "DFI_Money", "Dia", "District0x", "Dogecoin",
         "Enjin_Coin", "Enzyme", "EOS", "Ethereum", "Ethereum_Classic", "Ethereum_Name_Service", "Ethernity_Chain",
         "Fetch_ai", "Filecoin", "Function_Coin", "Gala", "Gitcoin", "Gods_Unchained", "Goldfinch", "Golem", "GYEN",
         "Harvest_Finance", "Highstreet", "Horizen", "IDEX", "iExec_RLC", "Immutable_X", "Internet_Computer",
         "Inverse_Finance", "IoTeX", "Jasmy", "Keep_Network", "Kryll", "Kyber_Network", "LCX", "Liquidity", "Litecoin",
         "Livepeer_LPT", "Loom_Network", "Loopring", "Maker", "Maple", "Mask_Network", "Measurable_Data_Token",
         "Mirror_Protocol", "Moss_Carbon_Credit", "mStableUSD", "My_Neighbor_Alice", "NKN", "NuCypher", "Numeraire",
         "OMG_Network", "Orca", "Orchid", "Origin_Token", "OriginTrail", "Orion_Protocol", "Pawtocol", "Paxos_Standard",
         "Perpetual_Protocol", "PlayDapp", "Pluton", "Polkadot", "Polkastarter", "Polygon", "Polymath", "Polyswarm",
         "Powerledger", "Propy", "Quant", "Quantstamp", "QuickSwap", "Radicle", "Rai_Reflex_Index", "Rally",
         "Rari_Governance_Token", "Rarible", "Ren", "Render_Token", "Request", "Ribbon_Finance", "Shapeshift_FOX_Token",
         "Shiba_Inu", "Shping_Coin", "SKALE", "Solana", "Spell_Token", "Stacks", "Status_Network", "Stellar_Lumens",
         "STORJ", "SUKU", "SuperFarm", "SushiSwap", "Synapse", "Synthetix_Network_Token", "Tellor", "TerraUSD",
         "Tether", "Tezos", "The_Graph", "Tribe", "TrueFi", "UMA", "Unifi_Protocol_DAO", "Uniswap",
         "Voyager_Token", "Wrapped_Bitcoin", "Wrapped_Centrifuge", "Wrapped_LUNA", "XYO_Network", "yearn_finance",
         "Zcash"]

coins_currency_codes = ["ZRX-USD", "1INCH-USD", "AAVE-USD", "AERGO-USD", "AIOZ-USD", "ALCX-USD", "ACH-USD", "AGLD-USD",
                        "ALGO-USD", "AMP-USD", "FORTH-USD", "ANKR-USD", "API3-USD", "ARPA-USD", "ASM-USD", "REP-USD",
                        "AVAX-USD", "AVT-USD", "AXS-USD", "BADGER-USD", "BAL-USD", "BNT-USD", "BAND-USD", "BOND-USD",
                        "BAT-USD", "BICO-USD", "BTC-USD", "BCH-USD", "BLZ-USD", "FIDA-USD", "AUCTION-USD", "BTRST-USD",
                        "ADA-USD", "CTSI-USD", "CGLD-USD", "LINK-USD", "CHZ-USD", "CVC-USD", "CLV-USD", "COMP-USD",
                        "ATOM-USD", "COTI-USD", "COVAL-USD", "CTX-USD", "CRO-USD", "CRV-USD", "DAI-USD", "DASH-USD",
                        "MANA-USD", "DESO-USD", "DDX-USD", "YFII-USD", "DIA-USD", "DNT-USD", "DOGE-USD", "ENJ-USD",
                        "MLN-USD", "EOS-USD", "ETH-USD", "ETC-USD", "ENS-USD", "ERN-USD", "FET-USD", "FIL-USD",
                        "FX-USD", "GALA-USD", "GTC-USD", "GODS-USD", "GFI-USD", "GLM-USD", "GYEN-USD", "FARM-USD",
                        "HIGH-USD", "ZEN-USD", "IDEX-USD", "RLC-USD", "IMX-USD", "ICP-USD", "INV-USD", "IOTX-USD",
                        "JASMY-USD", "KEEP-USD", "KRL-USD", "KNC-USD", "LCX-USD", "LQTY-USD", "LTC-USD", "LPT-USD",
                        "LOOM-USD", "LRC-USD", "MKR-USD", "MPL-USD", "MASK-USD", "MDT-USD", "MIR-USD", "MCO2-USD",
                        "MUSD-USD", "ALICE-USD", "NKN-USD", "NU-USD", "NMR-USD", "OMG-USD", "ORCA-USD", "OXT-USD",
                        "OGN-USD", "TRAC-USD", "ORN-USD", "UPI-USD", "PAX-USD", "PERP-USD", "PLA-USD", "PLU-USD",
                        "DOT-USD", "POLS-USD", "MATIC-USD", "POLY-USD", "NCT-USD", "POWR-USD", "PRO-USD", "QNT-USD",
                        "QSP-USD", "QUICK-USD", "RAD-USD", "RAI-USD", "RLY-USD", "RGT-USD", "RARI-USD", "REN-USD",
                        "RNDR-USD", "REQ-USD", "RBN-USD", "FOX-USD", "SHIB-USD", "SHPING-USD", "SKL-USD", "SOL-USD",
                        "SPELL-USD", "STX-USD", "SNT-USD", "XLM-USD", "STORJ-USD", "SUKU-USD", "SUPER-USD", "SUSHI-USD",
                        "SYN-USD", "SNX-USD", "TRB-USD", "UST-USD", "USDT-USD", "XTZ-USD", "GRT-USD",
                        "TRIBE-USD", "TRU-USD", "UMA-USD", "UNFI-USD", "UNI-USD", "VGX-USD", "WBTC-USD",
                        "WCFG-USD", "WLUNA-USD", "XYO-USD", "YFI-USD", "ZEC-USD"]

# for i in coins:
# mycursor.execute(f"DROP TABLE IF EXISTS {i}")

# The script below is for creating the database tables from my coins list.


# for i in coins:
# mycursor.execute(f"CREATE TABLE {i} (PRICE float, TOTAL_VOLUME float, 30_DAY_VOLUME float, "
#                      "OPENING_PRICE float, 24_HOUR_HIGH float,24_HOUR_LOW float, TIME datetime )")
# print(f"Table for {i} Successfully created")

counter = 0
print("Start Execution : ", end="")
print(time.ctime())
print()
while counter != 129600:
    try:
        for i in range(len(coins)):
            test1 = CoinObj.DatabaseInserter(coins_currency_codes[i], "test", "localhost", coins[i])
            test1.insertInformation()
            print(f"Successful insertion for {coins[i]}")
        counter += 1
        time.sleep(75)
    except:
        print("Your exception code ran.")
        for i in range(len(coins)):
            test1 = CoinObj.DatabaseInserter(coins_currency_codes[i], "test", "localhost", coins[i])
            test1.insertInformation()
            print(f"Successful insertion for {coins[i]}")
        counter += 1
        time.sleep(75)
 
print("Stop Execution : ", end="")
print(time.ctime())

# 10000 requests an hour
# Run the loop for 200 coins 50 times in an hour
# 3600 seconds in an hour
# The loop can be run a minimum every 72 seconds

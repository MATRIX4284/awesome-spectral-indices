from src.SpectralIndex import SpectralIndex
from typing import Dict
from pydantic import BaseModel


class SpectralIndices(BaseModel):
    SpectralIndices: Dict[str, SpectralIndex]


spindex = SpectralIndices(
    SpectralIndices=dict(
        BNDVI=SpectralIndex(
            short_name='BNDVI',
            long_name='Blue Normalized Difference Vegetation Index',
            formula='(N - B)/(N + B)',            
            reference='https://www.indexdatabase.de/db/i-single.php?id=135',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        CIG=SpectralIndex(
            short_name='CIG',
            long_name='Chlorophyll Index Green',
            formula='(N / G) - 1.0',            
            reference='https://doi.org/10.1078/0176-1617-00887',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        CVI=SpectralIndex(
            short_name='CVI',
            long_name='Chlorophyll Vegetation Index',
            formula='(N * R) / (G ** 2.0)',            
            reference='https://www.cabdirect.org/cabdirect/abstract/20073176046',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        EVI=SpectralIndex(
            short_name='EVI',
            long_name='Enhanced Vegetation Index',
            formula='g * (N - R) / (N + C1 * R - C2 * B + L)',            
            reference='https://doi.org/10.1016/S0034-4257(96)00112-5',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        EVI2=SpectralIndex(
            short_name='EVI2',
            long_name='Two-Band Enhanced Vegetation Index',
            formula='g * (N - R) / (N + 2.4 * R + L)',
            reference='https://doi.org/10.1016/j.rse.2008.06.006',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GARI=SpectralIndex(
            short_name='GARI',
            long_name='Green Atmospherically Resistant Vegetation Index',
            formula='(N - (G - (B - R))) / (N - (G + (B - R)))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=363',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GBNDVI=SpectralIndex(
            short_name='GBNDVI',
            long_name='Green-Blue Normalized Difference Vegetation Index',
            formula='(N - (G + B))/(N + (G + B))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=186',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GEMI=SpectralIndex(
            short_name='GEMI',
            long_name='Global Environment Monitoring Index',
            formula='((2.0*((N ** 2.0)-(R ** 2.0)) + 1.5*N + 0.5*R)/(N + R + 0.5))*(1.0 - 0.25*((2.0 * ((N ** 2.0) - (R ** 2)) + 1.5 * N + 0.5 * R)/(N + R + 0.5)))-((R - 0.125)/(1 - R))',
            reference='http://dx.doi.org/10.1007/bf00031911',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GLI=SpectralIndex(
            short_name='GLI',
            long_name='Green Leaf Index',
            formula='(2.0 * G - R - B) / (2.0 * G + R + B)',
            reference='http://dx.doi.org/10.1080/10106040108542184',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GNDVI=SpectralIndex(
            short_name='GNDVI',
            long_name='Green Normalized Difference Vegetation Index',
            formula='(N - G)/(N + G)',
            reference='https://doi.org/10.1016/S0034-4257(96)00072-7',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GRNDVI=SpectralIndex(
            short_name='GRNDVI',
            long_name='Green-Red Normalized Difference Vegetation Index',
            formula='(N - (G + R))/(N + (G + R))',
            reference='https://www.indexdatabase.de/db/i-single.php?id=185',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        GVMI=SpectralIndex(
            short_name='GVMI',
            long_name='Global Vegetation Moisture Index',
            formula='((N + 0.1) - (S2 + 0.02)) / ((N + 0.1) + (S2 + 0.02))',
            reference='https://doi.org/10.1016/S0034-4257(02)00037-8',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        MNDVI=SpectralIndex(
            short_name='MNDVI',
            long_name='Modified Normalized Difference Vegetation Index',
            formula='(N - S2)/(N + S2)',
            reference='https://doi.org/10.1080/014311697216810',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDVI=SpectralIndex(
            short_name='NDVI',
            long_name='Normalized Difference Vegetation Index',
            formula='(N - R)/(N + R)',
            reference='https://ntrs.nasa.gov/citations/19740022614',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NGRDI=SpectralIndex(
            short_name='NGRDI',
            long_name='Normalized Green Red Difference Index',
            formula='(G - R) / (G + R)',
            reference='https://doi.org/10.1016/0034-4257(79)90013-0',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        RVI=SpectralIndex(
            short_name='RVI',
            long_name='Ratio Vegetation Index',
            formula='N / R',
            reference='https://doi.org/10.2134/agronj1968.00021962006000060016x',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        SAVI=SpectralIndex(
            short_name='SAVI',
            long_name='Soil-Adjusted Vegetation Index',
            formula='(1.0 + L) * (N - R) / (N + R + L)',
            reference='https://doi.org/10.1016/0034-4257(88)90106-X',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        VARI=SpectralIndex(
            short_name='VARI',
            long_name='Visible Atmospherically Resistant Index',
            formula='(G - R) / (G + R - B)',
            reference='https://doi.org/10.1016/S0034-4257(01)00289-9',
            type='vegetation',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        BAI=SpectralIndex(
            short_name='BAI',
            long_name='Burned Area Index',
            formula='1.0 / ((0.1 - R) ** 2.0 + (0.06 - N) ** 2.0)',
            reference='https://digital.csic.es/bitstream/10261/6426/1/Martin_Isabel_Serie_Geografica.pdf',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        BAIS2=SpectralIndex(
            short_name='BAIS2',
            long_name='Burned Area Index for Sentinel 2',
            formula='(1.0 - ((RE2 * RE3 * RE4) / R) ** 0.5) * (((S2 - RE4)/(S2 + RE4) ** 0.5) + 1.0)',
            reference='https://doi.org/10.3390/ecrs-2-05177',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        CSIT=SpectralIndex(
            short_name='CSIT',
            long_name='Char Soil Index Thermal',
            formula='N / (S2 * T1 / 10000.0)',
            reference='https://doi.org/10.1080/01431160600954704',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NBR=SpectralIndex(
            short_name='NBR',
            long_name='Normalized Burn Ratio',
            formula='(N - S2) / (N + S2)',
            reference='https://www.usgs.gov/core-science-systems/nli/landsat/landsat-normalized-burn-ratio',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NBRT=SpectralIndex(
            short_name='NBRT',
            long_name='Normalized Burn Ratio Thermal',
            formula='(N - (S2 * T1 / 10000.0)) / (N + (S2 * T1 / 10000.0))',
            reference='https://doi.org/10.1080/01431160500239008',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDVIT=SpectralIndex(
            short_name='NDVIT',
            long_name='Normalized Difference Vegetation Index Thermal',
            formula='(N - (R * T1 / 10000.0))/(N + (R * T1 / 10000.0))',
            reference='https://doi.org/10.1080/01431160600954704',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        SAVIT=SpectralIndex(
            short_name='SAVIT',
            long_name='Soil-Adjusted Vegetation Index Thermal',
            formula='(1.0 + L) * (N - (R * T1 / 10000.0)) / (N + (R * T1 / 10000.0) + L)',
            reference='https://doi.org/10.1080/01431160600954704',
            type='burn',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        MNDWI=SpectralIndex(
            short_name='MNDWI',
            long_name='Modified Normalized Difference Water Index',
            formula='(G - S1) / (G + S1)',
            reference='https://doi.org/10.1080/01431160600589179',
            type='water',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDWI=SpectralIndex(
            short_name='NDWI',
            long_name='Normalized Difference Water Index',
            formula='(G - N) / (G + N)',
            reference='https://doi.org/10.1080/01431169608948714',
            type='water',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDSI=SpectralIndex(
            short_name='NDSI',
            long_name='Normalized Difference Snow Index',
            formula='(G - S1) / (G + S1)',
            reference='https://doi.org/10.1109/IGARSS.1994.399618',
            type='snow',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        NDDI=SpectralIndex(
            short_name='NDDI',
            long_name='Normalized Difference Drought Index',
            formula='(((N - R)/(N + R)) - ((G - N)/(G + N)))/(((N - R)/(N + R)) + ((G - N)/(G + N)))',
            reference='https://doi.org/10.1029/2006GL029127',
            type='drought',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        kEVI=SpectralIndex(
            short_name='kEVI',
            long_name='Kernel Enhanced Vegetation Index',
            formula='g * (kNN - kNR) / (kNN + C1 * kNR - C2 * kNB + kNL)',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-05-10',
            contributor="https://github.com/davemlz"
        ),
        kNDVI=SpectralIndex(
            short_name='kNDVI',
            long_name='Kernel Normalized Difference Vegetation Index',
            formula='(kNN - kNR)/(kNN + kNR)',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        kRVI=SpectralIndex(
            short_name='kRVI',
            long_name='Kernel Ratio Vegetation Index',
            formula='kNN / kNR',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-04-07',
            contributor="https://github.com/davemlz"
        ),
        kVARI=SpectralIndex(
            short_name='kVARI',
            long_name='Kernel Visible Atmospherically Resistant Index',
            formula='(kGG - kGR) / (kGG + kGR - kGB)',
            reference='https://doi.org/10.1126/sciadv.abc7447',
            type='kernel',
            date_of_addition='2021-05-10',
            contributor="https://github.com/davemlz"
        ),
        SeLI=SpectralIndex(
            short_name='SeLI',
            long_name='Sentinel-2 LAI Green Index',
            formula='(RE4 - RE1) / (RE4 + RE1)',
            reference='https://doi.org/10.3390/s19040904',
            type='vegetation',
            date_of_addition='2021-04-08',
            contributor="https://github.com/davemlz"
        ),
        OSAVI=SpectralIndex(
            short_name='OSAVI',
            long_name='Optimized Soil-Adjusted Vegetation Index',
            formula='(N - R) / (N + R + 0.16)',
            reference='https://doi.org/10.1016/0034-4257(95)00186-7',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        ARVI=SpectralIndex(
            short_name='ARVI',
            long_name='Atmospherically Resistant Vegetation Index',
            formula='(N - (R - gamma * (R - B))) / (N + (R - gamma * (R - B)))',
            reference='https://doi.org/10.1109/36.134076',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        SARVI=SpectralIndex(
            short_name='SARVI',
            long_name='Soil Adjusted and Atmospherically Resistant Vegetation Index',
            formula='(1 + L)*(N - (R - (R - B))) / (N + (R - (R - B)) + L)',
            reference='https://doi.org/10.1109/36.134076',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        NLI=SpectralIndex(
            short_name='NLI',
            long_name='Non-Linear Vegetation Index',
            formula='((N ** 2) - R)/((N ** 2) + R)',
            reference='https://doi.org/10.1080/02757259409532252',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        MNLI=SpectralIndex(
            short_name='MNLI',
            long_name='Modified Non-Linear Vegetation Index',
            formula='(1 + L)*((N ** 2) - R)/((N ** 2) + R + L)',
            reference='https://doi.org/10.1109/TGRS.2003.812910',
            type='vegetation',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        NMDI=SpectralIndex(
            short_name='NMDI',
            long_name='Normalized Multi-band Drought Index',
            formula='(N - (S1 - S2))/(N + (S1 - S2))',
            reference='https://doi.org/10.1029/2007GL031021',
            type='drought',
            date_of_addition='2021-05-11',
            contributor="https://github.com/davemlz"
        ),
        MSAVI=SpectralIndex(
            short_name='MSAVI',
            long_name='Modified Soil-Adjusted Vegetation Index',
            formula='0.5 * (2.0 * N + 1 - (((2 * N + 1) ** 2) - 8 * (N - R)) ** 0.5)',
            reference='https://doi.org/10.1016/0034-4257(94)90134-1',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        MCARI=SpectralIndex(
            short_name='MCARI',
            long_name='Modified Chlorophyll Absorption in Reflectance Index',
            formula='((RE1 - R) - 0.2 * (RE1 - G)) * (RE1 / R)',
            reference='http://dx.doi.org/10.1016/S0034-4257(00)00113-9',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        OCVI=SpectralIndex(
            short_name='OCVI',
            long_name='Optimized Chlorophyll Vegetation Index',
            formula='(N / G) * (R / G) ** cexp',            
            reference='http://dx.doi.org/10.1007/s11119-008-9075-z',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        NDREI=SpectralIndex(
            short_name='NDREI',
            long_name='Normalized Difference Red Edge Index',
            formula='(N - RE1) / (N + RE1)',            
            reference='https://doi.org/10.1016/1011-1344(93)06963-4',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        CIRE=SpectralIndex(
            short_name='CIRE',
            long_name='Chlorophyll Index Red Edge',
            formula='(N / RE1) - 1',            
            reference='https://doi.org/10.1078/0176-1617-00887',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        MTCI=SpectralIndex(
            short_name='MTCI',
            long_name='MERIS Terrestrial Chlorophyll Index',
            formula='(RE2 - RE1) / (RE1 - R)',            
            reference='https://doi.org/10.1080/0143116042000274015',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        TCARI=SpectralIndex(
            short_name='TCARI',
            long_name='Transformed Chlorophyll Absorption in Reflectance Index',
            formula='3 * ((RE1 - R) - 0.2 * (RE1 - G) * (RE1 / R))',
            reference='https://doi.org/10.1016/S0034-4257(02)00018-4',
            type='vegetation',
            date_of_addition='2021-05-13',
            contributor="https://github.com/davemlz"
        ),
        GDVI=SpectralIndex(
            short_name='GDVI',
            long_name='Generalized Difference Vegetation Index',
            formula='((N ** nexp) - (R ** nexp)) / ((N ** nexp) + (R ** nexp))',
            reference='https://doi.org/10.3390/rs6021211',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        WDRVI=SpectralIndex(
            short_name='WDRVI',
            long_name='Wide Dynamic Range Vegetation Index',
            formula='(alpha * N - R) / (alpha * N + R)',
            reference='https://doi.org/10.1078/0176-1617-01176',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MCARI1=SpectralIndex(
            short_name='MCARI1',
            long_name='Modified Chlorophyll Absorption in Reflectance Index 1',
            formula='1.2 * (2.5 * (N - R) - 1.3 * (N - G))',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MTVI1=SpectralIndex(
            short_name='MTVI1',
            long_name='Modified Triangular Vegetation Index 1',
            formula='1.2 * (1.2 * (N - G) - 2.5 * (R - G))',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MCARI2=SpectralIndex(
            short_name='MCARI2',
            long_name='Modified Chlorophyll Absorption in Reflectance Index 2',
            formula='(1.5 * (2.5 * (N - R) - 1.3 * (N - G))) / ((((2.0 * N + 1) ** 2) - (6.0 * N - 5 * (R ** 0.5)) - 0.5) ** 0.5)',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MTVI2=SpectralIndex(
            short_name='MTVI2',
            long_name='Modified Triangular Vegetation Index 2',
            formula='(1.5 * (1.2 * (N - G) - 2.5 * (R - G))) / ((((2.0 * N + 1) ** 2) - (6.0 * N - 5 * (R ** 0.5)) - 0.5) ** 0.5)',
            reference='https://doi.org/10.1016/j.rse.2003.12.013',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TVI=SpectralIndex(
            short_name='TVI',
            long_name='Triangular Vegetation Index',
            formula='0.5 * (120 * (N - G) - 200 * (R - G))',
            reference='http://dx.doi.org/10.1016/S0034-4257(00)00197-8',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MSR=SpectralIndex(
            short_name='MSR',
            long_name='Modified Simple Ratio',
            formula='(N / R - 1) / ((N / R + 1) ** 0.5)',
            reference='https://doi.org/10.1080/07038992.1996.10855178',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        RDVI=SpectralIndex(
            short_name='RDVI',
            long_name='Renormalized Difference Vegetation Index',
            formula='(N - R) / ((N + R) ** 0.5)',
            reference='https://doi.org/10.1016/0034-4257(94)00114-3',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        NDBI=SpectralIndex(
            short_name='NDBI',
            long_name='Normalized Difference Built-Up Index',
            formula='(S1 - N) / (S1 + N)',
            reference='http://dx.doi.org/10.1080/01431160304987',
            type='urban',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        MGRVI=SpectralIndex(
            short_name='MGRVI',
            long_name='Modified Green Red Vegetation Index',
            formula='(G ** 2.0 - R ** 2.0) / (G ** 2.0 + R ** 2.0)',
            reference='https://doi.org/10.1016/j.jag.2015.02.012',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        ExG=SpectralIndex(
            short_name='ExG',
            long_name='Excess Green Index',
            formula='2 * G - R - B',
            reference='https://doi.org/10.13031/2013.27838',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        DVI=SpectralIndex(
            short_name='DVI',
            long_name='Difference Vegetation Index',
            formula='N - R',
            reference='https://doi.org/10.2307/1936256',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        WDVI=SpectralIndex(
            short_name='WDVI',
            long_name='Weighted Difference Vegetation Index',
            formula='N - sla * R',
            reference='https://doi.org/10.1016/0034-4257(89)90076-X',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TSAVI=SpectralIndex(
            short_name='TSAVI',
            long_name='Transformed Soil-Adjusted Vegetation Index',
            formula='sla * (N - sla * R - slb) / (sla * N + R - sla * slb)',
            reference='https://doi.org/10.1109/IGARSS.1989.576128',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        ATSAVI=SpectralIndex(
            short_name='ATSAVI',
            long_name='Adjusted Transformed Soil-Adjusted Vegetation Index',
            formula='sla * (N - sla * R - slb) / (sla * N + R - sla * slb + 0.08 * (1 + sla ** 2.0))',
            reference='https://doi.org/10.1016/0034-4257(91)90009-U',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        SAVI2=SpectralIndex(
            short_name='SAVI2',
            long_name='Soil-Adjusted Vegetation Index 2',
            formula='N / (R + (slb / sla))',
            reference='https://doi.org/10.1080/01431169008955053',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TCI=SpectralIndex(
            short_name='TCI',
            long_name='Triangular Chlorophyll Index',
            formula='1.2 * (RE1 - G) - 1.5 * (R - G) * (RE1 / R) ** 0.5',
            reference='http://dx.doi.org/10.1109/TGRS.2007.904836',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        TGI=SpectralIndex(
            short_name='TGI',
            long_name='Triangular Greenness Index',
            formula='- 0.5 * (190 * (R - G) - 120 * (R - B))',
            reference='http://dx.doi.org/10.1016/j.jag.2012.07.020',
            type='vegetation',
            date_of_addition='2021-05-14',
            contributor="https://github.com/davemlz"
        ),
        IRECI=SpectralIndex(
            short_name='IRECI',
            long_name='Inverted Red-Edge Chlorophyll Index',
            formula='(RE3 - R) / (RE1 / RE2)',
            reference='https://doi.org/10.1016/j.isprsjprs.2013.04.007',
            type='vegetation',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        S2REP=SpectralIndex(
            short_name='S2REP',
            long_name='Sentinel-2 Red-Edge Position',
            formula='705.0 + 35.0 * ((((RE3 + R) / 2.0) - RE1) / (RE2 - RE1))',
            reference='https://doi.org/10.1016/j.isprsjprs.2013.04.007',
            type='vegetation',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        EBBI=SpectralIndex(
            short_name='EBBI',
            long_name='Enhanced Built-Up and Bareness Index',
            formula='(S1 - N) / (10.0 * ((S1 + T1) ** 0.5))',
            reference='https://doi.org/10.3390/rs4102957',
            type='urban',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        NDBaI=SpectralIndex(
            short_name='NDBaI',
            long_name='Normalized Difference Bareness Index',
            formula='(S1 - T1) / (S1 + T1)',
            reference='https://doi.org/10.1109/IGARSS.2005.1526319',
            type='urban',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        SIPI=SpectralIndex(
            short_name='SIPI',
            long_name='Structure Insensitive Pigment Index',
            formula='(N - A) / (N - R)',
            reference='https://eurekamag.com/research/009/395/009395053.php',
            type='vegetation',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        NHFD=SpectralIndex(
            short_name='NHFD',
            long_name='Non-Homogeneous Feature Difference',
            formula='(RE1 - A) / (RE1 + A)',
            reference='https://www.semanticscholar.org/paper/Using-WorldView-2-Vis-NIR-MSI-Imagery-to-Support-Wolf/5e5063ccc4ee76b56b721c866e871d47a77f9fb4',
            type='urban',
            date_of_addition='2021-09-17',
            contributor="https://github.com/davemlz"
        ),
        NDYI=SpectralIndex(
            short_name='NDYI',
            long_name='Normalized Difference Yellowness Index',
            formula='(G - B) / (G + B)',
            reference='https://doi.org/10.1016/j.rse.2016.06.016',
            type='vegetation',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        NRFIr=SpectralIndex(
            short_name='NRFIr',
            long_name='Normalized Rapeseed Flowering Index Red',
            formula='(R - S2) / (R + S2)',
            reference='https://doi.org/10.3390/rs13010105',
            type='vegetation',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        NRFIg=SpectralIndex(
            short_name='NRFIg',
            long_name='Normalized Rapeseed Flowering Index Green',
            formula='(G - S2) / (G + S2)',
            reference='https://doi.org/10.3390/rs13010105',
            type='vegetation',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        TRRVI=SpectralIndex(
            short_name='TRRVI',
            long_name='Transformed Red Range Vegetation Index',
            formula='((RE2 - R) / (RE2 + R)) / (((N - R) / (N + R)) + 1.0)',
            reference='https://doi.org/10.3390/rs12152359',
            type='vegetation',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        TTVI=SpectralIndex(
            short_name='TTVI',
            long_name='Transformed Triangular Vegetation Index',
            formula='0.5 * ((865.0 - 740.0) * (RE3 - RE2) - (RE4 - RE2) * (783.0 - 740))',
            reference='https://doi.org/10.3390/rs12010016',
            type='vegetation',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        NDSII=SpectralIndex(
            short_name='NDSII',
            long_name='Normalized Difference Snow Ice Index',
            formula='(R - S1) / (R + S1)',
            reference='https://doi.org/10.1080/01431160119766',
            type='snow',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        SWI=SpectralIndex(
            short_name='SWI',
            long_name='Snow Water Index',
            formula='(G * (N - S1)) / ((G + N) * (N + S1))',
            reference='https://doi.org/10.3390/rs11232774',
            type='snow',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        S3=SpectralIndex(
            short_name='S3',
            long_name='S3 Snow Index',
            formula='(N * (R - S1)) / ((N + R) * (N + S1))',
            reference='https://doi.org/10.3178/jjshwr.12.28',
            type='snow',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        WI1=SpectralIndex(
            short_name='WI1',
            long_name='Water Index 1',
            formula='(G - S2) / (G + S2)',
            reference='https://doi.org/10.3390/rs11182186',
            type='water',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        WI2=SpectralIndex(
            short_name='WI2',
            long_name='Water Index 2',
            formula='(B - S2) / (B + S2)',
            reference='https://doi.org/10.3390/rs11182186',
            type='water',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        AWEInsh=SpectralIndex(
            short_name='AWEInsh',
            long_name='Automated Water Extraction Index',
            formula='4.0 * (G - S1) - 0.25 * N + 2.75 * S2',
            reference='https://doi.org/10.1016/j.rse.2013.08.029',
            type='water',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        AWEIsh=SpectralIndex(
            short_name='AWEIsh',
            long_name='Automated Water Extraction Index with Shadows Elimination',
            formula='B + 2.5 * G - 1.5 * (N + S1) - 0.25 * S2',
            reference='https://doi.org/10.1016/j.rse.2013.08.029',
            type='water',
            date_of_addition='2021-09-18',
            contributor="https://github.com/davemlz"
        ),
        NBR2=SpectralIndex(
            short_name='NBR2',
            long_name='Normalized Burn Ratio 2',
            formula='(S1 - S2) / (S1 + S2)',
            reference='https://www.usgs.gov/core-science-systems/nli/landsat/landsat-normalized-burn-ratio-2',
            type='burn',
            date_of_addition='2021-09-20',
            contributor="https://github.com/davemlz"
        ),
        BWDRVI=SpectralIndex(
            short_name='BWDRVI',
            long_name='Blue Wide Dynamic Range Vegetation Index',
            formula='(alpha * N - B) / (alpha * N + B)',
            reference='https://doi.org/10.2135/cropsci2007.01.0031',
            type='vegetation',
            date_of_addition='2021-09-20',
            contributor="https://github.com/davemlz"
        ),
        ARI=SpectralIndex(
            short_name='ARI',
            long_name='Anthocyanin Reflectance Index',
            formula='(1 / G) - (1 / RE1)',
            reference='https://doi.org/10.1562/0031-8655(2001)074%3C0038:OPANEO%3E2.0.CO;2',
            type='vegetation',
            date_of_addition='2021-09-20',
            contributor="https://github.com/davemlz"
        ),
        VIG=SpectralIndex(
            short_name='VIG',
            long_name='Vegetation Index Green',
            formula='(G - R) / (G + R)',
            reference='https://doi.org/10.1016/S0034-4257(01)00289-9',
            type='vegetation',
            date_of_addition='2021-09-20',
            contributor="https://github.com/davemlz"
        ),
        VI700=SpectralIndex(
            short_name='VI700',
            long_name='Vegetation Index (700 nm)',
            formula='(RE1 - R) / (RE1 + R)',
            reference='https://doi.org/10.1016/S0034-4257(01)00289-9',
            type='vegetation',
            date_of_addition='2021-09-20',
            contributor="https://github.com/davemlz"
        ),
        VARI700=SpectralIndex(
            short_name='VARI700',
            long_name='Visible Atmospherically Resistant Index (700 nm)',
            formula='(RE1 - 1.7 * R + 0.7 * B) / (RE1 + 1.3 * R - 1.3 * B)',
            reference='https://doi.org/10.1016/S0034-4257(01)00289-9',
            type='vegetation',
            date_of_addition='2021-09-20',
            contributor="https://github.com/davemlz"
        ),
        TCARIOSAVI=SpectralIndex(
            short_name='TCARIOSAVI',
            long_name='TCARI/OSAVI Ratio',
            formula='(3 * ((RE1 - R) - 0.2 * (RE1 - G) * (RE1 / R))) / (1.16 * (N - R) / (N + R + 0.16))',
            reference='https://doi.org/10.1016/S0034-4257(02)00018-4',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        MCARIOSAVI=SpectralIndex(
            short_name='MCARIOSAVI',
            long_name='MCARI/OSAVI Ratio',
            formula='(((RE1 - R) - 0.2 * (RE1 - G)) * (RE1 / R)) / (1.16 * (N - R) / (N + R + 0.16))',
            reference='https://doi.org/10.1016/S0034-4257(00)00113-9',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        TCARIOSAVI705=SpectralIndex(
            short_name='TCARIOSAVI705',
            long_name='TCARI/OSAVI Ratio (705 and 750 nm)',
            formula='(3 * ((RE2 - RE1) - 0.2 * (RE2 - G) * (RE2 / RE1))) / (1.16 * (RE2 - RE1) / (RE2 + RE1 + 0.16))',
            reference='https://doi.org/10.1016/j.agrformet.2008.03.005',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        MCARIOSAVI705=SpectralIndex(
            short_name='MCARIOSAVI705',
            long_name='MCARI/OSAVI Ratio (705 and 750 nm)',
            formula='(((RE2 - RE1) - 0.2 * (RE2 - G)) * (RE2 / RE1)) / (1.16 * (RE2 - RE1) / (RE2 + RE1 + 0.16))',
            reference='https://doi.org/10.1016/j.agrformet.2008.03.005',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        MCARI705=SpectralIndex(
            short_name='MCARI705',
            long_name='Modified Chlorophyll Absorption in Reflectance Index (705 and 750 nm)',
            formula='((RE2 - RE1) - 0.2 * (RE2 - G)) * (RE2 / RE1)',
            reference='https://doi.org/10.1016/j.agrformet.2008.03.005',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        MSR705=SpectralIndex(
            short_name='MSR705',
            long_name='Modified Simple Ratio (705 and 750 nm)',
            formula='(RE2 / RE1 - 1) / ((RE2 / RE1 + 1) ** 0.5)',
            reference='https://doi.org/10.1016/j.agrformet.2008.03.005',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        NDVI705=SpectralIndex(
            short_name='NDVI705',
            long_name='Normalized Difference Vegetation Index (705 and 750 nm)',
            formula='(RE2 - RE1) / (RE2 + RE1)',
            reference='https://doi.org/10.1016/S0176-1617(11)81633-0',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        SR705=SpectralIndex(
            short_name='SR705',
            long_name='Simple Ratio (705 and 750 nm)',
            formula='RE2 / RE1',
            reference='https://doi.org/10.1016/S0176-1617(11)81633-0',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        SR555=SpectralIndex(
            short_name='SR555',
            long_name='Simple Ratio (555 and 750 nm)',
            formula='RE2 / G',
            reference='https://doi.org/10.1016/S0176-1617(11)81633-0',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        REDSI=SpectralIndex(
            short_name='REDSI',
            long_name='Red-Edge Disease Stress Index',
            formula='((705.0 - 665.0) * (RE3 - R) - (783.0 - 665.0) * (RE1 - R)) / (2.0 * R)',
            reference='https://doi.org/10.3390/s18030868',
            type='vegetation',
            date_of_addition='2021-11-06',
            contributor="https://github.com/davemlz"
        ),
        NIRv=SpectralIndex(
            short_name='NIRv',
            long_name='Near-Infrared Reflectance of Vegetation',
            formula='((N - R) / (N + R)) * N',
            reference='https://doi.org/10.1126/sciadv.1602244',
            type='vegetation',
            date_of_addition='2021-11-16',
            contributor="https://github.com/davemlz"
        ),
        AFRI2100=SpectralIndex(
            short_name='AFRI2100',
            long_name='Aerosol Free Vegetation Index (2100 nm)',
            formula='(N - 0.5 * S2) / (N + 0.5 * S2)',
            reference='https://doi.org/10.1016/S0034-4257(01)00190-0',
            type='vegetation',
            date_of_addition='2021-11-17',
            contributor="https://github.com/davemlz"
        ),
        AFRI1600=SpectralIndex(
            short_name='AFRI1600',
            long_name='Aerosol Free Vegetation Index (1600 nm)',
            formula='(N - 0.66 * S1) / (N + 0.66 * S1)',
            reference='https://doi.org/10.1016/S0034-4257(01)00190-0',
            type='vegetation',
            date_of_addition='2021-11-17',
            contributor="https://github.com/davemlz"
        ),
        NIRvP=SpectralIndex(
            short_name='NIRvP',
            long_name='Near-Infrared Reflectance of Vegetation and Incoming PAR',
            formula='((N - R) / (N + R)) * N * PAR',
            reference='https://doi.org/10.1016/j.rse.2021.112763',
            type='vegetation',
            date_of_addition='2021-11-18',
            contributor="https://github.com/davemlz"
        ),
        NDMI=SpectralIndex(
            short_name='NDMI',
            long_name='Normalized Difference Moisture Index',
            formula='(N - S1)/(N + S1)',
            reference='https://doi.org/10.1016/S0034-4257(01)00318-2',
            type='vegetation',
            date_of_addition='2021-12-01',
            contributor="https://github.com/bpurinton"
        ),
        QpRVI=SpectralIndex(
            short_name='QpRVI',
            long_name='Quad-Polarized Radar Vegetation Index',
            formula='(8.0 * HV)/(HH + VV + 2.0 * HV)',
            reference='https://doi.org/10.1109/IGARSS.2001.976856',
            type='radar',
            date_of_addition='2021-12-24',
            contributor="https://github.com/davemlz"
        ),
        RFDI=SpectralIndex(
            short_name='RFDI',
            long_name='Radar Forest Degradation Index',
            formula='(HH - HV)/(HH + HV)',
            reference='https://doi.org/10.5194/bg-9-179-2012',
            type='radar',
            date_of_addition='2021-12-25',
            contributor="https://github.com/davemlz"
        ),
        DpRVIHH=SpectralIndex(
            short_name='DpRVIHH',
            long_name='Dual-Polarized Radar Vegetation Index HH',
            formula='(4.0 * HV)/(HH + HV)',
            reference='https://www.tandfonline.com/doi/abs/10.5589/m12-043',
            type='radar',
            date_of_addition='2021-12-25',
            contributor="https://github.com/davemlz"
        ),
        DpRVIVV=SpectralIndex(
            short_name='DpRVIVV',
            long_name='Dual-Polarized Radar Vegetation Index VV',
            formula='(4.0 * VH)/(VV + VH)',
            reference='https://doi.org/10.3390/app9040655',
            type='radar',
            date_of_addition='2021-12-25',
            contributor="https://github.com/davemlz"
        ),
        NWI=SpectralIndex(
            short_name='NWI',
            long_name='New Water Index',
            formula='(B - (N + S1 + S2))/(B + (N + S1 + S2))',
            reference='https://doi.org/10.11873/j.issn.1004-0323.2009.2.167',
            type='water',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        WRI=SpectralIndex(
            short_name='WRI',
            long_name='Water Ratio Index',
            formula='(G + R)/(N + S1)',
            reference='https://doi.org/10.1109/GEOINFORMATICS.2010.5567762',
            type='water',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        NDVIMNDWI=SpectralIndex(
            short_name='NDVIMNDWI',
            long_name='NDVI-MNDWI Model',
            formula='((N - R)/(N + R)) - ((G - S1)/(G + S1))',
            reference='https://doi.org/10.1007/978-3-662-45737-5_51',
            type='water',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        MBWI=SpectralIndex(
            short_name='MBWI',
            long_name='Multi-Band Water Index',
            formula='(omega * G) - R - N - S1 - S2',
            reference='https://doi.org/10.1016/j.jag.2018.01.018',
            type='water',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        GCC=SpectralIndex(
            short_name='GCC',
            long_name='Green Chromatic Coordinate',
            formula='G / (R + G + B)',
            reference='https://doi.org/10.1016/0034-4257(87)90088-5',
            type='vegetation',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        RCC=SpectralIndex(
            short_name='RCC',
            long_name='Red Chromatic Coordinate',
            formula='R / (R + G + B)',
            reference='https://doi.org/10.1016/0034-4257(87)90088-5',
            type='vegetation',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        BCC=SpectralIndex(
            short_name='BCC',
            long_name='Blue Chromatic Coordinate',
            formula='B / (R + G + B)',
            reference='https://doi.org/10.1016/0034-4257(87)90088-5',
            type='vegetation',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        NIRvH2=SpectralIndex(
            short_name='NIRvH2',
            long_name='Hyperspectral Near-Infrared Reflectance of Vegetation',
            formula='N - R - k * (lambdaN - lambdaR)',
            reference='https://doi.org/10.1016/j.rse.2021.112723',
            type='vegetation',
            date_of_addition='2022-01-17',
            contributor="https://github.com/davemlz"
        ),
        NDPI=SpectralIndex(
            short_name='NDPI',
            long_name='Normalized Difference Phenology Index',
            formula='(N - (alpha * R + (1.0 - alpha) * S1))/(N + (alpha * R + (1.0 - alpha) * S1))',
            reference='https://doi.org/10.1016/j.rse.2017.04.031',
            type='vegetation',
            date_of_addition='2022-01-20',
            contributor="https://github.com/davemlz"
        ),
        NDII=SpectralIndex(
            short_name='NDII',
            long_name='Normalized Difference Infrared Index',
            formula='(N - S1)/(N + S1)',
            reference='https://www.asprs.org/wp-content/uploads/pers/1983journal/jan/1983_jan_77-83.pdf',
            type='vegetation',
            date_of_addition='2022-01-20',
            contributor="https://github.com/davemlz"
        ),
        DVIplus=SpectralIndex(
            short_name='DVIplus',
            long_name='Difference Vegetation Index Plus',
            formula='((lambdaN - lambdaR)/(lambdaN - lambdaG)) * G + (1.0 - ((lambdaN - lambdaR)/(lambdaN - lambdaG))) * N - R',
            reference='https://doi.org/10.1016/j.rse.2019.03.028',
            type='vegetation',
            date_of_addition='2022-01-20',
            contributor="https://github.com/davemlz"
        ),
        NDGI=SpectralIndex(
            short_name='NDGI',
            long_name='Normalized Difference Greenness Index',
            formula='(((lambdaN - lambdaR)/(lambdaN - lambdaG)) * G + (1.0 - ((lambdaN - lambdaR)/(lambdaN - lambdaG))) * N - R)/(((lambdaN - lambdaR)/(lambdaN - lambdaG)) * G + (1.0 - ((lambdaN - lambdaR)/(lambdaN - lambdaG))) * N + R)',
            reference='https://doi.org/10.1016/j.rse.2019.03.028',
            type='vegetation',
            date_of_addition='2022-01-20',
            contributor="https://github.com/davemlz"
        ),
        FCVI=SpectralIndex(
            short_name='FCVI',
            long_name='Fluorescence Correction Vegetation Index',
            formula='N - ((R + G + B)/3.0)',
            reference='https://doi.org/10.1016/j.rse.2020.111676',
            type='vegetation',
            date_of_addition='2022-01-20',
            contributor="https://github.com/davemlz"
        ),
        UI=SpectralIndex(
            short_name='UI',
            long_name='Urban Index',
            formula='(S2 - N)/(S2 + N)',
            reference='https://www.isprs.org/proceedings/XXXI/congress/part7/321_XXXI-part7.pdf',
            type='urban',
            date_of_addition='2022-02-07',
            contributor="https://github.com/davemlz"
        ),
        VrNIRBI=SpectralIndex(
            short_name='VrNIRBI',
            long_name='Visible Red-Based Built-Up Index',
            formula='(R - N)/(R + N)',
            reference='https://doi.org/10.1016/j.ecolind.2015.03.037',
            type='urban',
            date_of_addition='2022-02-09',
            contributor="https://github.com/davemlz"
        ),
        VgNIRBI=SpectralIndex(
            short_name='VgNIRBI',
            long_name='Visible Green-Based Built-Up Index',
            formula='(G - N)/(G + N)',
            reference='https://doi.org/10.1016/j.ecolind.2015.03.037',
            type='urban',
            date_of_addition='2022-02-09',
            contributor="https://github.com/davemlz"
        ),
        IBI=SpectralIndex(
            short_name='IBI',
            long_name='Index-Based Built-Up Index',
            formula='(((S1-N)/(S1+N))-(((N-R)*(1.0+L)/(N+R+L))+((G-S1)/(G+S1)))/2.0)/(((S1-N)/(S1+N))+(((N-R)*(1.0+L)/(N+R+L))+((G-S1)/(G+S1)))/2.0)',
            reference='https://doi.org/10.1080/01431160802039957',
            type='urban',
            date_of_addition='2022-02-09',
            contributor="https://github.com/davemlz"
        ),
        BLFEI=SpectralIndex(
            short_name='BLFEI',
            long_name='Built-Up Land Features Extraction Index',
            formula='(((G+R+S2)/3.0)-S1)/(((G+R+S2)/3.0)+S1)',
            reference='https://doi.org/10.1080/10106049.2018.1497094',
            type='urban',
            date_of_addition='2022-02-09',
            contributor="https://github.com/davemlz"
        ),
    )
)

\# 🌱 AgriMate – Smart Farming Assistant



AgriMate is an AI-powered Smart Farming Assistant designed to help farmers make better agricultural decisions using Machine Learning, Deep Learning and digital farming tools.



\## 🚜 Features



\### 🌾 Crop Recommendation

AgriMate recommends a suitable crop using:



\- Nitrogen (N)

\- Phosphorus (P)

\- Potassium (K)

\- Temperature

\- Humidity

\- Soil pH

\- Rainfall



A Random Forest Machine Learning model is used for crop prediction.



\### 🌿 Plant Disease Detection



Farmers can upload a plant leaf image.



AgriMate uses a Convolutional Neural Network (CNN) to predict the possible plant disease.



The system also provides general disease management guidance when information is available.



\### 🛒 Agricultural Marketplace



The marketplace provides:



\- Seeds

\- Plants

\- Fertilizers

\- Farming Tools

\- Irrigation Equipment



It includes:



\- Product search

\- Category filtering

\- Recommended products

\- Shopping cart

\- Cart total



\### 🛠️ Farming Tools



AgriMate provides useful agricultural calculators including:



\- Land Area Calculator

\- Irrigation Water Calculator

\- Fertilizer Calculator

\- Crop Profit Calculator



\### 🔐 Login / Signup



Users can create an account and log in to access the Farmer Dashboard.



\### 📊 Farmer Dashboard



The dashboard provides quick access to:



\- Crop Recommendation

\- Disease Detection

\- Marketplace

\- Farming Tools

\- Shopping Cart

\- AgriMate system status



\---



\# 🤖 AI Technologies



\## Crop Recommendation



\*\*Algorithm:\*\* Random Forest



\*\*Dataset:\*\* Crop Recommendation Dataset



\*\*Input Features:\*\*



N, P, K, temperature, humidity, pH and rainfall.



\## Plant Disease Detection



\*\*Algorithm:\*\* Convolutional Neural Network (CNN)



\*\*Framework:\*\* PyTorch



\*\*Dataset:\*\* PlantVillage



\*\*Classes:\*\* 38



\---



\# 🏗️ System Architecture



```text

&#x20;                   🌱 AGRIMATE

&#x20;                        |

&#x20;             -----------------------

&#x20;             |                     |

&#x20;       Streamlit Frontend      FastAPI Backend

&#x20;             |                     |

&#x20;     -------------------      -------------

&#x20;     |        |        |      |           |

&#x20;    Crop   Disease  Marketplace  ML Model  CNN

&#x20;     |        |        |      |           |

&#x20;     |        |        |   Random Forest  |

&#x20;     |        |        |                  |

&#x20;     |        |        |              PlantVillage

&#x20;     |

&#x20;  Farming Tools

&#x20;     |

&#x20;  Farmer Dashboard


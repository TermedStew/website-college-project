import requests
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "Cosmic Forge", page_icon = "logo.png", layout = "wide")

rtx4090 = Image.open("rtx4090.png")
rx6800 = Image.open("rx6800.png")
corei9 = Image.open("corei9.png")
amdcpu = Image.open("amdcpu.png")
corsair = Image.open("corsair.png")
trident = Image.open("trident.png")
realchart = Image.open("chart.png")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

lottie_gpu = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_gysbecac.json")
lottie_cpu = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_15bffwea.json")
lottie_lap = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_contact = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_y3qfynfr.json")
lottie_hire = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_cjkryupy.json")
lottie_call = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_lstnp9p3.json")
with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ["Home", "Store", "About Us", "Contact Us"],
        icons = ["house", "cart", "person", "envelope"],
        menu_icon = None,
        orientation = "vertical",
        default_index = 0,
        styles = {
            "container" : {"padding" : "0!important", "background-color" : "#2eccfa"},
            "icon" : {"color" : "#b4edfd", "font-size" : "20px"},
            "nav-link" : {
                "font-size" : "20px",
                "text-align" : "left",
                "margin" : "5px",
                "--hover-color" : "#67dafb",
            },

            "nav-link-selected" : {"background-color" : "#08c3f9"},

        },
    )

hide_st_style = """
                <style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                """

st.markdown(hide_st_style, unsafe_allow_html = True)

logo = Image.open("logo.png")

if selected == "Home":
    with st.container():
        image_col, text_col = st.columns((1, 5))
        with text_col:
            st.title("Cosmic Forge")
            st.subheader("We provide the best and high quality products.")
        with image_col:
            st.image(logo, width = 150)
    st.write("---")
    st.title("Home")
    with st.container():
        lottie1, lottie2, lottie3 = st.columns(3)
        with lottie1:
            st_lottie(lottie_gpu)
        with lottie2:
            st_lottie(lottie_cpu)
        with lottie3:
            st_lottie(lottie_lap)
    st.title("Cosmic Forge")
    st.subheader("Cosmic Forge is a new, up-and-coming Computer company that provides customers with the newest, cutting-edge technology you'll find in the market today. It provides multiple products and services such as computer parts, computer assembly, cleaning of rigs and many more to come.")
if selected == "Store":
    st.title("Store")
    products, services = st.tabs(["Products", "Services"])
    with products:
        st.title("GPU")
        st.write("---")
        with st.container():
            rtx4090_pic, rtx4090_desc = st.columns((3, 2))
        with rtx4090_pic:
            st.image(rtx4090, width = 500)
        with rtx4090_desc:
            st.subheader("[RTX 4090](https://www.nvidia.com/en-ph/geforce/graphics-cards/40-series/rtx-4090/)")
            st.write("NVIDIA CUDA Cores      | 16384")
            st.write("Boost Clock (GHz)      | 2.52")
            st.write("Memory Size            | 24GB")
            st.write("Memory Type            | GDDR6X")
            st.write("Max Display Resolution | 4K at 240Hz / 8K at 60Hz, with DSC")

        with st.container():
            rx6800_pic, rx6800_desc = st.columns((3, 2))
        with rx6800_pic:
            st.image(rx6800, width = 500)
        with rx6800_desc:
            st.subheader("[RX 6800 XT](https://www.amd.com/en/products/graphics/amd-radeon-rx-6800-xt)")
            st.write("Stream Processors      | 16384")
            st.write("Boost Frequency (MHz)  | 2250")
            st.write("Memory Size            | 16GB")
            st.write("Memory Type            | GDDR6")
            st.write("Max Display Resolution | HDMI 4K / 4K H264")

        st.title("CPU")
        st.write("---")
        with st.container():
            intel_i9_pic, intel_i9_desc = st.columns((3, 2))
        with intel_i9_pic:
            st.image(corei9, width = 500)
        with intel_i9_desc:
            st.subheader("[Intel Core i9 10850K](https://ark.intel.com/content/www/us/en/ark/products/205904/intel-core-i910850k-processor-20m-cache-up-to-5-20-ghz.html)")
            st.write("Total Cores            | 10")
            st.write("Total Threads          | 20")
            st.write("Max Turbo Frequency    | 5.20GHz")
            st.write("Memory Type            | DDR4-2933")
            st.write("4K Support             | 60Hz")
            st.write("DirectX Support        | 12")
            st.write("OpenGL Support         | 4.5")
        with st.container():
            amdcpu_pic, amdcpu_desc = st.columns((3, 2))
        with amdcpu_pic:
            st.image(amdcpu, width = 500)
        with amdcpu_desc:
            st.subheader("[AMD Ryzen 5 5600X](https://www.amd.com/en/products/cpu/amd-ryzen-5-5600x)")
            st.write("Total Cores            | 6")
            st.write("Total Threads          | 12")
            st.write("Max Boost Clock        | 4.6GHz")
            st.write("Base clock             | 3.7GHz")
            st.write("L2 Cache               | 3MB")
            st.write("L3 Cache               | 32MB")
        st.title("RAM")
        st.write("---")
        with st.container():
            corsair_pic, corsair_desc = st.columns((3, 2))
        with corsair_pic:
            st.image(corsair, width = 500)
        with corsair_desc:
            st.subheader("[Corsair Vengeance LED 32GB (2x16GB)](https://www.corsair.com/us/en/Categories/Products/Memory/vengeance-led-configurator/p/CMU32GX4M2C3000C15)")
            st.write("Memory Speed           | 3000MHz")
            st.write("Size                   | 32GB")
            st.write("RAM Memory             | DDR4")
            st.title("")
            st.title("")
            st.title("")
            st.title("")
            st.title("")
        with st.container():
            tridentr_pic, trident_desc = st.columns((3, 2))
        with corsair_pic:
            st.image(trident, width = 500)
        with corsair_desc:
            st.subheader("[Trident Z RGB DC](https://www.gskill.com/product/165/296/1552456723/F4-3200C14D-64GTZDC-EOL)")
            st.write("Memory Speed           | 3200MHz")
            st.write("Size                   | 64GB")
            st.write("RAM Memory             | DDR4")
        st.write("---")
        st.title("New Products Coming Soon")
    with services:
        st.write("Contact Us")
        st.write("[Pre-Built PC] [PC Cleaning] [PC/Parts Repair]")
        contact_form = """
        <form action="https://formsubmit.co/cosmicforgecontact@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="What service do you like?" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        con_left, con_right = st.columns((2, 2))
        with con_left:
            st.markdown(contact_form, unsafe_allow_html=True)
        with con_right:
            st_lottie(lottie_contact)

if selected == "About Us":
    st.title("Cosmic Forge Organizational Chart")
    st.write("---")
    st.image("chart.png", width = 950)
    hire, anim = st.columns((1, 1))
    with hire:
        st.subheader("For more hiring information, contact us through our contact page.")
        st.subheader("We are hiring for:")
        st.subheader("- Inventory Planners")
        st.subheader("- Project Managers")
        st.subheader("- Producers")
    with anim:
        st_lottie(lottie_hire)
    st.write("---")
    vision, mission = st.columns(2)
    with vision:
        st.title("VISION")
        st.subheader("To be a customer-focused computer service company and to provide a space where anybody can come"
                     "and find high-quality, valuable outputs and designs to buy at a fair price.")
    with mission:
        st.title("MISSION")
        st.subheader("Cosmic Forge is focusing on becoming a highly credible and productive computer service company"
                     "backed by customer care. ")
    st.write("---")
    st.write("We are a group of college students tasked to make our own website.")


if selected == "Contact Us":
    st.title("CONTACT US")
    st.write("---")
    contactus_form = """
            <form action="https://formsubmit.co/cosmicforgecontact@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
    con_left, con_right = st.columns(2)
    with con_left:
        st.markdown(contactus_form, unsafe_allow_html=True)
    with con_right:
        st_lottie(lottie_call)
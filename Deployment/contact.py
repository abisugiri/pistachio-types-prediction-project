import streamlit as st

def run():
    # Title
    st.title('Contacts')
    st.markdown('---')
    st.write('###### For further information, you can contact the author.')
    st.markdown('---')
    
    st.write('##### Author Contact Information:')
    st.write('[GITHUB](https://github.com/abisugiri)')
    st.write('or')
    st.write('[LINKEDIN](https://www.linkedin.com/in/abi-sugiri/)')


if __name__ == '__main__':
    run()
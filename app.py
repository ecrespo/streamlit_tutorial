import streamlit as st



def calculate_sum(n1:int, n2:int)-> int:
    return int(n1) + int(n2)



def main():
    st.title('Add numbers')
    n1 = st.text_input('First number')
    n2 = st.text_input('Second number')

    if st.button('Add'):
        result = calculate_sum(n1, n2)
        st.success(result)
        st.write('The sum of {} and {} is {}'.format(n1, n2, result))


if __name__ == '__main__':
    main()

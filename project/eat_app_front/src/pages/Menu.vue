<template>
    <div v-if="isData === true">
        <NavBar/>
        <h1 class="page_category">Меню</h1>
        <ul>
            <li class="dish_element" v-for="elem in dishes" :key="elem.id">
                <div class="dish_name"><h2>{{elem.dish_name}}</h2></div>
                <div class="dish_compose">{{elem.dish_compose}}</div>
                <div class="dish_price"><h3>{{elem.dish_price}} руб.</h3></div>
                <div class="line"></div>
            </li>
        </ul>
    </div>
    <div v-else>
        <h1>Page not found</h1>
    </div>
</template>

<script>
import NavBar from "@/Components/NavBar.vue";
import axios from "axios";

export default {
    data() {
        return {
            dishes: [],
            isData: false,
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/dish_view/')
            .then(response => {
                this.dishes = response.data
                this.isData = true
            })
            .catch(error => {
                self.isData = false
                console.log(error);
            });
    },
    components: {NavBar},
}

</script>

<style lang="scss">
.dish_name{
    font-family: 'Roboto Condensed', sans-serif;
}

.dish_price{
    font-family: 'Roboto Condensed', sans-serif;
}
</style>
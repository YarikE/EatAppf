<template>
    <NavBar/>
    <h1 class="page_category">Приложение для заказа корпоративной еды</h1>
    <div class="text-center">
        <img src="../static/main3.jpg" alt="Изображение" class="rounded" height="585">
    </div>
</template>

<script>
import NavBar from "@/Components/NavBar.vue";
export default {
    components: {NavBar},
}


</script>

<style lang="scss" scoped>
.page_category {
    margin-bottom: 1%;
    text-align: center;
}
img{
    margin-bottom: 2%;
}
</style>
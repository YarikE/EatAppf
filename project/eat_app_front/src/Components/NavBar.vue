<template>
    <div class="navigation">
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <a class="navbar-brand text-light" href="#">EatApp</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse px-4"  id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <router-link class="nav-link text-light px-5" to="/">Главная</router-link>
                        </li>

                        <li class="nav-item text-light">
                            <router-link class="nav-link text-light px-5" to="/menu">Меню</router-link>
                        </li>

                        <li class="nav-item">
                            <router-link class="nav-link text-light px-5" to="/order">Заказ</router-link>
                        </li>

                        <li class="nav-item">
                            <router-link class="nav-link text-light px-5" to="/history">История заказов пользователя</router-link>
                        </li>

                        <li class="nav-item">
                            <router-link class="nav-link text-light px-5" to="/lucky">Мне повезет</router-link>
                        </li>

                        <li class="nav-item">
                            <router-link class="nav-link text-light px-5" to="/report">Отчет "Заказы на дату"</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>

    .navigation{
        background-color: deepskyblue;
    }

    .nav-link{
        color: white;
    } 
    .navbar-nav me-auto mb-2 mb-lg-0{
        display: inline-block;
    }

    .nav-item{
        font-family: 'Pacifico', cursive;
    }

    router-link{
        white-space: nowrap;
    }
    a{
        font-family: 'Lobster', cursive;
    }
</style>
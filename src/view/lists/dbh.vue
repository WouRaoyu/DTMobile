<!--
 * @ Author: WouRaoyu
 * @ Create Time: 2024-07-09 16:44:34
 * @ Modified by: WouRaoyu
 * @ Modified time: 2024-07-09 17:44:14
 * @ Description:
 -->

 <template>
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
        <van-list v-model:loading="loading" :finished="finished" finished-text="没有更多了" @load="onLoad">
            <van-cell-group inset v-for="item in list" :key="item">
                <van-cell title="单元格" value="内容" label="描述信息">
                    <van-tag type="primary">状态</van-tag>
                </van-cell>
            </van-cell-group>
        </van-list>
    </van-pull-refresh>
</template>

<script>
import { ref } from 'vue';

export default {
    setup() {
        const list = ref([]);
        const loading = ref(false);
        const finished = ref(false);
        const refreshing = ref(false);

        const onLoad = () => {
            setTimeout(() => {
                if (refreshing.value) {
                    list.value = [];
                    refreshing.value = false;
                }

                for (let i = 0; i < 10; i++) {
                    list.value.push(list.value.length + 1);
                }
                loading.value = false;

                if (list.value.length >= 40) {
                    finished.value = true;
                }
            }, 1000);
        };

        const onRefresh = () => {
            // 清空列表数据
            finished.value = false;

            // 重新加载数据
            // 将 loading 设置为 true，表示处于加载状态
            loading.value = true;
            onLoad();
        };

        return {
            list,
            onLoad,
            loading,
            finished,
            onRefresh,
            refreshing,
        };
    },
};
</script>

<style>
:root {
    --van-cell-group-inset-padding: var(--van-padding-md)
}
</style>
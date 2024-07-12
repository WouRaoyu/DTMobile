<!--
 * @ Author: WouRaoyu
 * @ Create Time: 2024-07-09 16:45:29
 * @ Modified by: WouRaoyu
 * @ Modified time: 2024-07-09 21:51:45
 * @ Description:
 -->

<template>
    <van-tabs v-model:active="active" scrollspy sticky>
        <van-tab title="基础信息">
            <van-cell-group inset>
                <van-cell title="工程名称" value="康定2号隧道2#斜井" />
                <van-cell title="施工里程" value="X1DK2+869.0" />
                <van-cell title="开挖宽度" value="8.16m" />
                <van-cell title="开挖高度" value="7.73m" />
                <van-cell title="开挖方式" value="全断面" />
                <van-cell title="岩石类型" value="二长花岗岩" />
            </van-cell-group>
        </van-tab>
        <van-tab title="综合结论">
            <van-cell-group inset>
                <van-cell>
                    <!-- <span class="center-span">综合结论</span> -->
                    掌子面揭示围岩主要为二长花岗岩，深灰色、灰褐色，局部夹灰白色，弱风化为主，节理裂隙较发育，节理面多侵染，主要两组节理产状：N45°W/75°NE、N65°E/90°，掌子面发育石英脉，宽5～15cm，围岩整体较完整，拱顶局部较破碎，掌子面整体湿润，渗水，掌子面及拱顶多处呈股状出水，掌子面后方呈淋雨状滴水，局部呈股状出水。
                </van-cell>
            </van-cell-group>
        </van-tab>
        <van-tab title="围岩等级">
            <van-cell-group inset>
                <van-cell title="单元格">
                    <van-tag type="primary">状态</van-tag>
                </van-cell>
                <van-image width="100%" src="https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg" />
            </van-cell-group>
        </van-tab>
        <van-tab title="破碎程度">
            <van-cell-group inset>
                <van-cell title="单元格" value="内容" label="描述信息">
                    <van-tag type="primary">状态</van-tag>
                </van-cell>
                <van-image width="100%" src="https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg" />
            </van-cell-group>
        </van-tab>
        <van-tab title="坚硬程度">
            <van-cell-group inset>
                <van-cell title="单元格" value="内容" label="描述信息">
                    <van-tag type="primary">状态</van-tag>
                </van-cell>
                <van-image width="100%" src="https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg" />
            </van-cell-group>
        </van-tab>
        <van-tab title="富水程度">
            <van-cell-group inset>
                <van-cell title="单元格" value="内容" label="描述信息">
                    <van-tag type="primary">状态</van-tag>
                </van-cell>
                <van-image width="100%" src="https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg" />
            </van-cell-group>
        </van-tab>
        <van-tab title="地应力状态">
            <van-cell-group inset>
                <van-cell title="单元格" value="内容" label="描述信息">
                    <van-tag type="primary">状态</van-tag>
                </van-cell>
                <van-image width="100%" src="https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg" />
            </van-cell-group>
        </van-tab>
        <van-tab title="高清影像">
            <van-cell-group inset>
                <van-cell title="单元格" value="内容" label="描述信息">
                    <van-tag type="primary">状态</van-tag>
                </van-cell>
                <van-image width="100%" src="https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg" />
            </van-cell-group>
        </van-tab>
    </van-tabs>
</template>

<script>
export default {
    mounted() {
        alert(this.$route.query.id);
    }
}
</script>

<style>
:root {
    --van-cell-group-inset-padding: var(--van-padding-md)
}

.center-span {
    display: block;
    width: 100%;
    text-align: center;
}
</style>
<template>
	<div id="div_aside_mask" :class="parm_bool_AsideIsOpen?'m_active':''">
	</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
	name: "AsideMask",
	data(): any {
		return {};
	},
	props: {
		parm_bool_AsideIsOpen: {
			type: Boolean,
			default: false,
		},
	},
});
</script>

<style lang="sass">
@import "@/components/viewport"
@import "@/components/component"
$AsideAnimateTime: 0.2s
#div_aside_mask
    transition: background $AsideAnimateTime ease-in-out
    @media #{$aboveTablet}
        display: none
    &.m_active
        position: fixed
        background-color: rgba(0,0 ,0 ,0.5 )
        width: 100%
        height: 100vh
        top: 0
        left: 0
        z-index: $layer_navMask!important
</style>
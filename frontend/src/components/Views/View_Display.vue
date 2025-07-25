<!-- src/components/Views -->
<script setup lang="ts">
  import { ref, type DefineComponent } from 'vue'

  import Shipment_Component from '@/components/Views/Shipment_View.vue';
  import Process_Component from '@/components/Views/Process_View.vue';
  import Order_Component from '@/components/Views/Order_View.vue';
  import Resource_Component from '@/components/Views/Inventory_View.vue';

  type ComponentType = DefineComponent<{}, {}, any>

  const componentMap = {
    shipments: Shipment_Component,
    processes: Process_Component,
    orders: Order_Component,
    resources: Resource_Component,
  } satisfies Record<string, ComponentType>

  const currentComponent = ref<ComponentType>(componentMap.shipments)

  type ComponentKey = keyof typeof componentMap
  const currentname = ref<ComponentKey>('shipments')

  function setComponent(name: keyof typeof componentMap) {
    currentComponent.value = componentMap[name]
    currentname.value = name
  }

</script>

<template>
  <div class="component-frame">
    <div class="component-choice-frame">
      <h3 class="component-name">{{ currentname }}</h3>
      <div class="component-menu-frame">
        <h6>choose view</h6>
        <ul class="component-menu">
          <li><button @click="setComponent('resources')" class="scroll-button">Resources</button></li>
          <li><button @click="setComponent('shipments')" class="scroll-button">Shipments</button></li>
          <li><button @click="setComponent('processes')" class="scroll-button">Processes</button></li>
          <li><button @click="setComponent('orders')" class="scroll-button">Orders</button></li>
        </ul>
      </div>
    </div id="component-container">
    <component :is="currentComponent" />
  </div>
</template>

<style>
  .component-choice-frame {
    display: flex;
    border: 2px solid #555;
    box-sizing: border-box;
    height: 3rem;
  }

  .component-name {
    flex: 2 1 0;
    box-sizing: border-box;
    line-height: 0.6;
  }

  .component-menu-frame {
    flex: 1 1 0;
    border: 2px solid #555;
    box-sizing: border-box;
  }

  .component-menu-frame h6{
    line-height: 0;
  }

  .component-menu {
    display: inline-block;
    top: calc(50% + .25rem);      
    left: 0;
    max-height: 160px;             
    overflow-y: auto;              
    background:#333;
    padding:2px 2px;
    margin: 0;
    list-style:none;
    box-shadow:0 8px 18px rgba(0,0,0,.5);

    opacity: 0;
    transform: translateY(-8px);
    visibility: hidden;
    transition: opacity .25s ease, transform .25s ease;
  }

  .component-menu-frame:hover .component-menu {
    opacity: 1;
    transform: translateY(0);
    visibility: visible;
  }
    
  .scroll-button {
    display:block;
    padding:0 1rem;
    text-decoration:none;
    color:#36499f;
    font-size:.9rem;
    width: 100%
  }
</style>